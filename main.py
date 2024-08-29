import requests

# Replace with your personal access token
GITHUB_TOKEN = "YOUR-API-KEY"
USERNAME = "YOUR-USER-NAME"

# Headers with authorization
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Function to get the list of repositories
def get_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return [repo['name'] for repo in response.json()]
    else:
        print(f"Failed to fetch repositories: {response.status_code}")
        return []

# Get repository traffic views
def get_repo_views(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/traffic/views"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch views for {repo}: {response.status_code}")
        return None

# Get repository traffic clones
def get_repo_clones(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/traffic/clones"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch clones for {repo}: {response.status_code}")
        return None

# Fetch repositories
repositories = get_repositories(USERNAME)

# Loop through the repositories and fetch traffic data
for repo in repositories:
    views = get_repo_views(USERNAME, repo)
    clones = get_repo_clones(USERNAME, repo)
    print(f"Repository: {repo}")
    print("Views:", views)
    print("Clones:", clones)
    print("-------------")
