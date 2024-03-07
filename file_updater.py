import git
import json
import os


def write_json(data, filepath):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)


def update_lol_file(filename, lol_filepath):
    """
    Update the League of Legends (LoL) file with new data.

    Args:
        data: The new data to be added to the LoL file.
        lol_filepath: The file path to the LoL file.

    Returns:
        None
    """

    lol_filepath += "\Config\ItemSets.json"
    
    with open(lol_filepath) as old_lol_file, open(f"champions/{filename}") as data:
        lol_data = json.load(old_lol_file)
        lol_data["itemSets"].append(json.load(data))
    write_json(lol_data, lol_filepath)


def update_local_files(folder):
    """
    Update local files by pulling the specified repository. If the repository does not exist, clone it and print an error message.

    :param folder: the folder to update
    :return: None
    """
    try:
        git.Repo(folder).remotes.origin.pull()
    except git.exc.NoSuchPathError:
        git.Repo.clone_from(
            'https://github.com/Ganii7/Runeitems-champions.git', folder)
        print("Error to pull, cloning repository")


if __name__ == "__main__":
    file = r"champions"
    update_local_files(file)
    for filename in os.listdir("./champions"):
        if filename.endswith(".json"):
            update_lol_file(filename, r"C:\Games\Riot Games\League of Legends")
            print(filename)
