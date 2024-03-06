import git


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
    file = r"../champions"
    update_local_files(file)
