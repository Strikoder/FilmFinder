import streamlit as st
import pickle
import pandas as pd
import requests

# choosed to read the pickle from pd cause it caused an error through pickle library
pickled_df = pd.read_pickle(open('../model/movies.pkl', 'rb'))
similarity = pickle.load(open('../model/similarity.pkl', 'rb'))
movies_list = pickled_df['title'].values


def fetch_poster(movie_id):
    api_key = "Your API key"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    request = requests.get(url)
    data = request.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    recommended_movie_names = []
    recommended_movies_posters = []
    movie_index = pickled_df[pickled_df['title'] == movie].index[0]
    # it has a tuple of the index and similarity score of the top 5 similar movies
    simlr_movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    for elem in simlr_movies_list:
        movie_id = pickled_df.iloc[elem[0]].movie_id
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
        # receiving the movie id then asserting its title
        recommended_movie_names.append(pickled_df.iloc[elem[0]].title)

    return recommended_movie_names, recommended_movies_posters


st.title("Film Recommender")

selected_movie_name = st.selectbox(
    "Choose your film",
    movies_list)

if st.button("Recommend"):
    recommended_movie_name, recommended_movie_poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_movie_name[0])
        st.image(recommended_movie_poster[0])
    with col2:
        st.text(recommended_movie_name[1])
        st.image(recommended_movie_poster[1])

    with col3:
        st.text(recommended_movie_name[2])
        st.image(recommended_movie_poster[2])
    with col4:
        st.text(recommended_movie_name[3])
        st.image(recommended_movie_poster[3])
    with col5:
        st.text(recommended_movie_name[4])
        st.image(recommended_movie_poster[4])
