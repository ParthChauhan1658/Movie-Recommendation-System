# Movie-Recommendation-System
This project is a Movie Recommendation System that suggests movies to users based on their preferences or similarities with other movies. The system leverages machine learning techniques such as collaborative filtering, content-based filtering, or hybrid approaches to provide personalized recommendations.

## Dataset
The dataset used in this project is sourced from [MovieLens](https://grouplens.org/datasets/movielens/?spm=5aebb161.6a10b3ed.0.0.3d845171EJ3gEB), a popular dataset for building recommendation systems. It includes the following key features:
- User ID : Unique identifier for each user.
- Movie ID : Unique identifier for each movie.
- Ratings : Ratings given by users to movies (1–5 scale).
- Movie Titles : Names of the movies.
- Genres : Categories or genres associated with each movie (e.g., Action, Comedy, Drama).
- The dataset is preprocessed to handle missing values, encode categorical variables, and prepare it for training recommendation models.

## How to Use
1. Install Python 3.x from [python.org](https://www.python.org/downloads/?spm=5aebb161.6a10b3ed.0.0.3d845171EJ3gEB) 
2. Install the required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```
4. Clone the Repository :
   ```bash 
   git clone https://github.com/ParthChauhan1658/Movie-Recommendation-System.git
   cd Movie-Recommendation-System
   ```
5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
6. Input a user ID and movie genres or movie title to get personalized recommendations.

## Techniques Used
- **Exploratory Data Analysis (EDA)** : Analyzed user behavior, movie popularity, and rating distributions.
- **Collaborative Filtering** : Found patterns among users with similar tastes to recommend movies.
- **Content-Based Filtering** : Recommended movies similar to ones the user has liked based on genres and metadata.
- **Hybrid Approach** : Combined collaborative and content-based filtering for improved accuracy.
- **Model Training** : Trained recommendation models using libraries like scikit-learn and surprise.

## Deployment
The app can be deployed on platforms like [Streamlit Cloud](https://streamlit.io/cloud) or Heroku for public access
