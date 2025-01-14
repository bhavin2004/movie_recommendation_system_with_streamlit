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

if (not os.path.exists('artifacts/similarity.pkl')):
            train_pipe_obj = Training_Pipeline()
            train_pipe_obj.run_pipeline()
        

df = pd.read_csv('artifacts/processed_data/data.csv')

st.title("Movie Recommandation System")


movie = st.selectbox(
    "Select The Movie from Below:-",
    set(df['title'].to_list())
)


if st.button("Recommand the Movies"):
    predict_obj = PredictionPipeline()
    recommended_movies=predict_obj.run_pipeline(movie=movie)
    for movie_id,movie_name in recommended_movies.items():
        
        st.write(movie_id)
        st.write(fetch_poster(movie_id=movie_id))
        st.write(movie_name)
    # st.write(recommended_movies)
    # st.write(type(recommended_movies))
    # for i in recommended_movies:
    #     st.write(i)