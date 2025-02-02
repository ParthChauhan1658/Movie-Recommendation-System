import streamlit as st
import pandas as pd

# Load the datasets
movies = pd.read_csv('movies.csv')  # Corrected file name
ratings = pd.read_csv('ratings.csv')  # Corrected file name

# Content-Based Recommendation Functions

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

# Streamlit App
st.title("Movie Recommendation System")

# Check if the user is new
user_id = st.number_input("Enter User ID (or 0 for first-time users):", min_value=0, max_value=ratings['userId'].max(), value=0)

if user_id == 0:
    st.write("Welcome! Let's get to know your preferences.")
    
    # Option 1: Select favorite genres
    all_genres = set('|'.join(movies['genres']).split('|'))
    preferred_genres = st.multiselect("Select your favorite genres:", list(all_genres))
    
    # Option 2: Select a recently liked movie
    recently_liked_movie = st.selectbox("Select a movie you recently liked:", movies['title'])
    
    if st.button("Get Recommendations"):
        # Step 1: Recommend movies based on genres
        if preferred_genres:
            st.write("\nBased on your preferred genres:")
            genre_recommendations = recommend_by_genre(preferred_genres, movies)
            st.table(genre_recommendations[['title', 'genres']])
        
        # Step 2: Recommend movies similar to the recently liked movie
        if recently_liked_movie:
            st.write(f"\nBased on your recently liked movie '{recently_liked_movie}':")
            similar_movie_recommendations = recommend_similar_movies(recently_liked_movie, movies)
            st.table(similar_movie_recommendations[['title', 'genres']])
else:
    st.write("Returning users are currently handled by collaborative filtering.")
    # You can integrate collaborative filtering here if needed
