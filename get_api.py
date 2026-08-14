import requests

base_url = "https://api.github.com/users"

def github_user(username):
    url = f"{base_url}/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    
    return None

def repo_details(username):
        
        url = f"{base_url}/{username}/repos"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        
        return []