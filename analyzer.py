import pandas as pd
import numpy as np

def repositories_to_dataframe(repositories):
    df = pd.DataFrame(repositories)
    
    return df

def analyze_repositories(df):
    
    results = {}
    
    # no of repo
    
    results["total_repositories"] = len(df)
    
    # most used language
    
    languages = df["language"].dropna()
    
    if len(languages)> 0:
        results["top_language"] = languages.value_counts().index[0]
        
    else:
        results["top_language"] = "unknown"
        
     # average star   

    stars = df["stargazers_count"].fillna(0).to_numpy()
    results["average_stars"] = np.mean(stars)
    
    # maximum stars
    
    results["maximum_stars"] = np.max(stars)
    
    #star variation 
    
    results["star_std"] = np.std(stars)
    
    return results