from git import Repo

def pull_repository():
    Repo("../champions").remotes.origin.pull()

def clone_repository():
    Repo.clone_from('https://github.com/Ganii7/Runeitems-champions.git', r'../champions')
    
#if __name__ == "__main__":
#   pull_repository()