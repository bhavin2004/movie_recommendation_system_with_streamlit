import streamlit as st
from src.movie_recommendation_system.pipelines.predicrion_pipeline import (
    PredictionPipeline
)
from src.movie_recommendation_system.pipelines.training_pipeline import (
    Training_Pipeline
)
from src.utlis import fetch_poster
import pandas as pd
import os

# Check if similarity.pkl exists, if not, run the training pipeline
if not os.path.exists('artifacts/similarity.pkl'):
    train_pipe_obj = Training_Pipeline()
    train_pipe_obj.run_pipeline()

# Load the processed data
df = pd.read_csv('artifacts/processed_data/data.csv')

# Set the app title
st.title("Movie Recommendation System")

# Movie selection dropdown
movie = st.selectbox(
    "Select a Movie from Below:",
    df['title'].to_list()
)

# Recommendation button
if st.button("Recommend Movies"):
    predict_obj = PredictionPipeline()
    recommended_movies = predict_obj.run_pipeline(movie=movie)

    # Extract movie IDs and names
    movie_ids = list(recommended_movies.keys())
    movie_names = list(recommended_movies.values())

    # Create a row of 5 columns for recommendations
    cols = st.columns(5, gap='medium')
    for index, col in enumerate(cols):
        with col:
            # Center-align the text and image
            st.markdown(f"### {movie_names[index]}")
            st.image(fetch_poster(movie_id=movie_ids[index]), use_column_width=True)
