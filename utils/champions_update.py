from git import Repo

def pull_repository(folder):
    Repo(folder).remotes.origin.pull()
    
def clone_repository(folder):
    Repo.clone_from('https://github.com/Ganii7/Runeitems-champions.git', folder)
    
if __name__ == "__main__":
    file = r"../champions"
    try:
        pull_repository(file)
    except:
        clone_repository(file)
        print("Error to pull, cloning repository")