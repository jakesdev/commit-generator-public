import os
import random
from datetime import datetime, timedelta
from git import Repo
import time

REPO_PATH = 'D:\Workspace\commit-generator'
COMMIT_FILE = 'commit_log.txt'
COMMIT_MESSAGES = [
    'Update documentation', 'Fix bug', 'Add feature', 'Refactor code',
    'Update dependencies', 'Optimize performance', 'Add tests',
    'Clean up code', 'Improve UI/UX', 'Fix typo'
]

def append_commit(date):
    timestamp = date.strftime('%Y%m%d_%H%M%S')
    message = f"{random.choice(COMMIT_MESSAGES)}_{timestamp}"
    filepath = os.path.join(REPO_PATH, COMMIT_FILE)
    
    with open(filepath, 'a') as f:
        f.write(f'Auto-commit at {timestamp}\n')
    return COMMIT_FILE, message

def generate_random_time():
    return random.randint(9, 18), random.randint(0, 59), random.randint(0, 59)

def perform_yearly_commits():
    repo = Repo(REPO_PATH)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    current_date = start_date

    while current_date <= end_date:
        num_commits = random.randint(5, 20)
        
        for _ in range(num_commits):
            try:
                hour, minute, second = generate_random_time()
                commit_datetime = current_date.replace(hour=hour, minute=minute, second=second)
                
                filename, message = append_commit(commit_datetime)
                repo.index.add([filename])
                
                commit_timestamp = commit_datetime.strftime('%Y-%m-%d %H:%M:%S')
                new_env = os.environ.copy()
                new_env['GIT_AUTHOR_DATE'] = commit_timestamp
                new_env['GIT_COMMITTER_DATE'] = commit_timestamp
                
                repo.index.commit(message, author_date=commit_timestamp, commit_date=commit_timestamp)
                print(f'Created commit: {message} at {commit_timestamp}')
                time.sleep(0.1)
                
            except Exception as e:
                print(f'Error during commit: {e}')
        
        current_date += timedelta(days=1)
        
        if current_date.weekday() == 6:
            try:
                origin = repo.remote('origin')
                origin.push(force=True)
                print('Pushed week of commits')
            except Exception as e:
                print(f'Error during push: {e}')

    try:
        origin = repo.remote('origin')
        origin.push(force=True)
        print('Final push completed')
    except Exception as e:
        print(f'Error during final push: {e}')

if __name__ == '__main__':
    perform_yearly_commits()
