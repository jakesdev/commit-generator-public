import os
import random
from datetime import datetime
from git import Repo

REPO_PATH = 'D:\Workspace\commit-generator'
COMMIT_FILE = 'commit_log.txt'
COMMIT_MESSAGES = [
    'Update documentation', 'Fix bug', 'Add feature', 'Refactor code',
    'Update dependencies', 'Optimize performance', 'Add tests',
    'Clean up code', 'Improve UI/UX', 'Fix typo'
]

def append_commit():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    message = f"{random.choice(COMMIT_MESSAGES)}_{timestamp}"
    filepath = os.path.join(REPO_PATH, COMMIT_FILE)
    
    with open(filepath, 'a') as f:
        f.write(f'Auto-commit at {timestamp}\n')
    return COMMIT_FILE, message

def perform_commits():
    repo = Repo(REPO_PATH)
    num_commits = random.randint(5, 10)
    
    for _ in range(num_commits):
        try:
            filename, message = append_commit()
            repo.index.add([filename])
            repo.index.commit(message)
            print(f'Created commit: {message}')
        except Exception as e:
            print(f'Error during commit: {e}')
    
    try:
        origin = repo.remote('origin')
        origin.push()
        print(f'Pushed {num_commits} commits')
    except Exception as e:
        print(f'Error during push: {e}')

if __name__ == '__main__':
    perform_commits()
