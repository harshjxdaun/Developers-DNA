# project: guthub analyzer
from get_api import github_user, repo_details
from analyzer import repositories_to_dataframe,analyze_repositories

print("="*40)
print("     GITHUB PROFILE ANALYZER   ")
print("="*40)

#get github profile

username = input("Enter your username here : ")
user = github_user(username)



if user is None:
    print("User not found !!")
    
else:
    print("User: ", user["name"])
    print("Followers: ", user["followers"])
    print("repositories:", user["public_repos"])
    
    #get repo
        
    repositories = repo_details(username)
        
    # convert data into DataFrame
    
    df = repositories_to_dataframe(repositories)
    
    #analyze data
    
    results = analyze_repositories(df)
    
    #display analysis
    
    print("============ANALYSIS=============")
    
    print("Total repositories: " ,
          results["total_repositories"]
        )
    
    print("Top language: " ,
          results["top_language"]
        )
    
    print("Maximun stars:",
          results["maximum_stars"]
        )
    print("Star standard deviation: ",
          round(results["star_std"])
        )