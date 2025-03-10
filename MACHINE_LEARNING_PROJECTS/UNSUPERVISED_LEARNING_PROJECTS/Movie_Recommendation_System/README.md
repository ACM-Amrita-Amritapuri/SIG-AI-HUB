# Movie Recommendation System

## Overview
This project is a movie recommendation system that uses KMeans clustering to group similar genres together and recommend movies based on either a movie title or a genre provided by the user. The system is built using Python and Tkinter for the GUI.

## Work Flow
1.**Importing Libraries:**
    Necessary libraries are imported for data manipulation, machine learning, and gui.
    
2.**Loading Dataset:**
    The IMDB dataset is loaded into a pandas DataFrame. The head() method displays the first few rows of the dataset.

3.**Preprocess the data:**
    Ensure your dataset includes the necessary columns for movie IDs, titles, and genres. 
    The dataset should be in CSV format and should include columns representing different genres as binary indicators (e.g., Action, Comedy, Drama, etc.).
    
4.**Determine the Optimal Number of Clusters:**
    Use the Elbow Method to determine the optimal number of clusters. 
    This involves plotting the sum of squared errors (SSE) for a range of cluster values and identifying the "elbow point" where the SSE starts to decrease more slowly.

5.**Cluster the Movies:**
    Once the optimal number of clusters is determined, apply K-means clustering to assign each movie to a cluster. 
   
6.**Make Recommendations:**
    For a given movie, the system can then recommend other movies from the same cluster.
    Or for a given genre, it will recommend corresponding movies.

## Elbow Method
  **Purpose:** Determines the optimal number of clusters for K-means clustering.
  **Procedure:** Iteratively applies K-means clustering with different numbers of clusters, calculates the sum of squared errors (SSE) for each number of clusters, and plots these SSE values to identify the elbow point.
