import pandas as pd

# Step 1: Load the datasets
movies = pd.read_csv('movies.csv')  # Corrected file name
ratings = pd.read_csv('ratings.csv')  # Corrected file name

# Display the first few rows of each dataset
print("Movies Dataset:")
print(movies.head())
print("\nRatings Dataset:")
print(ratings.head())

# Step 2: Exploratory Data Analysis (EDA)
# Check the shape of the datasets
print("\nShape of Movies Dataset:", movies.shape)
print("Shape of Ratings Dataset:", ratings.shape)

# Check for missing values
print("\nMissing Values in Movies Dataset:")
print(movies.isnull().sum())
print("\nMissing Values in Ratings Dataset:")
print(ratings.isnull().sum())

# Step 3: Content-Based Recommendation Functions

# Function to recommend movies based on preferred genres
def recommend_by_genre(preferred_genres, movies, n_recommendations=5):
    """
    Recommends movies based on the user's preferred genres.
    """
    recommended_movies = movies[
        movies['genres'].apply(lambda x: any(genre in x.split('|') for genre in preferred_genres))
    ].head(n_recommendations)
    return recommended_movies

# Function to recommend movies similar to a specific movie
def recommend_similar_movies(movie_title, movies, n_recommendations=5):
    """
    Recommends movies similar to the given movie based on shared genres.
    """
    # Find the genres of the input movie
    try:
        movie_genres = movies[movies['title'] == movie_title]['genres'].iloc[0].split('|')
    except IndexError:
        return "Movie not found in the dataset."
    
    # Recommend movies with similar genres
    recommended_movies = movies[
        movies['genres'].apply(lambda x: any(genre in x.split('|') for genre in movie_genres))
    ].head(n_recommendations)
    
    # Exclude the input movie itself
    recommended_movies = recommended_movies[recommended_movies['title'] != movie_title]
    
    return recommended_movies

# Step 4: Onboarding Process for First-Time Users
def onboard_user():
    print("Welcome! Let's get to know your preferences.")
    
    # Option 1: Select favorite genres
    print("\nSelect your favorite genres from the list below:")
    all_genres = set('|'.join(movies['genres']).split('|'))
    print(", ".join(all_genres))
    preferred_genres = input("Enter your favorite genres (comma-separated): ").split(',')
    preferred_genres = [genre.strip() for genre in preferred_genres]
    
    # Option 2: Select a recently liked movie
    recently_liked_movie = input("\nEnter a movie you recently liked: ")
    
    return preferred_genres, recently_liked_movie

# Step 5: Main Recommendation Logic
def recommend_movies(user_id, ratings, movies):
    # Check if the user is new
    if user_id not in ratings['userId'].unique():
        print("First-time user detected!")
        
        # Step 1: Onboard the user
        preferred_genres, recently_liked_movie = onboard_user()
        
        # Step 2: Recommend movies based on genres
        print("\nBased on your preferred genres:")
        genre_recommendations = recommend_by_genre(preferred_genres, movies)
        print(genre_recommendations)
        
        # Step 3: Recommend movies similar to the recently liked movie
        print(f"\nBased on your recently liked movie '{recently_liked_movie}':")
        similar_movie_recommendations = recommend_similar_movies(recently_liked_movie, movies)
        print(similar_movie_recommendations)
    else:
        print("Returning users are currently handled by collaborative filtering.")
        # You can integrate collaborative filtering here if needed

# Step 6: Test the Recommendation System
# Example: Recommend movies for User 1
user_id = 1
recommend_movies(user_id, ratings, movies)
