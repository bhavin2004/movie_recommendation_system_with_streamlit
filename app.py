import streamlit as st
from src.movie_recommendation_system.pipelines.predicrion_pipeline import (
    PredictionPipeline,
)
from src.movie_recommendation_system.pipelines.training_pipeline import (
    Training_Pipeline,
)
# from src.u
import pandas as pd

df = pd.read_csv('artifacts/processed_data/data.csv')

st.title("Movie Recommandation System")


movie = st.selectbox(
    "Select The Movie from Below:-",
    set(df['title'].to_list())
)


if st.button("Recommand the Movies"):
    predict_obj = PredictionPipeline()
    recommended_movies=predict_obj.run_pipeline(movie=movie)
    for movie_id,movie_name in recommended_movies:
        st.write(movie_id)
        st.write(movie_name)
    st.write(recommended_movies)