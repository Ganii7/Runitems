import git


def pull_repository(folder):
    git.Repo(folder).remotes.origin.pull()


def clone_repository(folder):
    git.Repo.clone_from(
        'https://github.com/Ganii7/Runeitems-champions.git', folder)


def update_local_files(file):
    try:
        pull_repository(file)
    except git.exc.NoSuchPathError:
        clone_repository(file)
        print("Error to pull, cloning repository")


if __name__ == "__main__":
    file = r"../champions"
    update_local_files(file)
