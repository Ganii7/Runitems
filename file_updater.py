import git
import json
import os


def write_json(data, filepath):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)


def update_lol_file(filename, lol_filepath):
    """
    Updates a League of Legends file with new item sets.

    Parameters:
    - filename: a string representing the name of the file to be updated
    - lol_filepath: a string representing the path to the League of Legends file

    Return:
    This function does not return anything.
    """
    lol_filepath += "\Config\ItemSets.json"

    with open(lol_filepath) as old_lol_file, open(f"champions/{filename}") as data:
        lol_data = json.load(old_lol_file)
        lol_data["itemSets"].append(json.load(data))
    write_json(lol_data, lol_filepath)


def update_local_files(switch):
    """
    Updates local files by pulling changes from the remote git repository.

    Args:
        switch (bool): A boolean flag indicating whether to create all lanes git repo.

    Returns:
        None
    """
    try:
        git.Repo(r"champions").remotes.origin.pull()
    except git.exc.NoSuchPathError:
        if switch:
            # TODO: create all lanes git repo
            # TODO: add all lanes git
            print("pls create all lanes git")
        else:
            git.Repo.clone_from(
                'https://github.com/Ganii7/Runeitems-champions.git', r"champions")
        print("Error to pull, cloning repository")


def main(switch):
    if switch:
        # TODO: import all lanes
        print("import all lanes")
        # update_local_files(switch)
        # for filename in os.listdir("./champions"):
        #     if filename.endswith(".json"):
        #         update_lol_file(filename, r"C:\Riot Games\League of Legends")
        #         print(filename)
    else:
        print("import most popular lane")
        # update_local_files(switch)
        # for filename in os.listdir("./champions"):
        #     if filename.endswith(".json"):
        #         update_lol_file(filename, r"C:\Riot Games\League of Legends")
        #         print(filename)


if __name__ == "__main__":
    main(False)
