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
if st.button("Recommend the Movies"):
    predict_obj = PredictionPipeline()
    recommended_movies = predict_obj.run_pipeline(movie=movie)
    movie_id = list(recommended_movies.keys())
    movie_name = list(recommended_movies.values())

    # Display recommended movies in a row
    for index, col in enumerate(st.columns(5, gap='medium')):
        with col:
            st.image(fetch_poster(movie_id=movie_id[index]), use_container_width=True)
            st.write(f"<p style='text-align: center;'>{movie_name[index]}</p>", unsafe_allow_html=True)
