# project: guthub analyzer

import requests

def github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    
    return None

def repo_details(username):
        
        url = f"https://api.github.com/users/{username}/repos"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        
        return []

print("="*40)
print("     GITHUB PROFILE ANALYZER   ")
print("="*40)

username = input("Enter your username here : ")
user = github_user(username)

if user is None:
    print("User not found !!")
    
else:
    def user_info():
        print("========PROFILE========")
        print("Username:", user["login"])
        print("Name:", user["name"])
        print("Bio:", user["bio"])
        print("Followers:", user["followers"])
        print("Following:", user["following"])
        print("Public repositories:", user["public_repos"])
    
    user_info()
    
    
    repositories = repo_details(username)
    
    print("\n=======REPOSITORIES========")
    
    for repo in repositories:
        print(repo["name"])
    
    
    