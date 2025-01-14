# Movie Recommendation System with Streamlit  

A **Movie Recommendation System** built using Python and Streamlit, which provides personalized movie recommendations based on a hybrid approach combining **Bag of Words** and **Word2Vec** techniques.  

---

## Features  
- Recommends movies based on a selected movie title.  
- Displays recommended movie titles along with their posters.  
- Interactive user interface built with Streamlit.  
- Automatically trains the model if similarity metrics are not precomputed.  

---

## Technologies Used  
- **Python**  
- **Streamlit** for the user interface.  
- **Pandas** for data manipulation.  
- **NLTK** for text preprocessing.  
- **Scikit-learn** for machine learning models.  
- **NumPy** for numerical computations.  

---

## How It Works  
1. **Hybrid Recommendation System**:  
   - **Bag of Words**: Captures textual similarity between movie descriptions.  
   - **Word2Vec**: Captures semantic similarity between movie descriptions.  
   - Combines both approaches to provide accurate and personalized recommendations.  

2. **Pipeline Structure**:  
   - **Training Pipeline**: Prepares and saves the similarity metrics.  
   - **Prediction Pipeline**: Retrieves and processes recommendations based on user input.  

3. **Poster Fetching**: Uses the movie's unique ID to fetch posters dynamically.  

---

## Installation  

### Prerequisites  
- Python 3.7 or above installed.  
- Libraries: `pandas`, `numpy`, `nltk`, `scikit-learn`, `streamlit`.  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/bhavin2004/movie_recommendation_system_with_streamlit.git  
   cd movie_recommendation_system_with_streamlit  
