import pandas as pd
import streamlit as st
import pickle
import requests

tmdb_api = "00f9a9bd252c595f5381cf4ad18557f4"

movies_list = pickle.load(open('movies.pkl','rb'))
movies_df = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    api = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api}&language=en-US"
    movie_data = requests.get(api).json()
    return 'http://image.tmdb.org/t/p/w500' + movie_data['poster_path']

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_list = []
    recommended_movies_posters_list = []
    for i in movie_list:
        recommended_movies_list.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters_list.append(fetch_poster(movies_df.iloc[i[0]].movie_id))
    return recommended_movies_list, recommended_movies_posters_list

st.title("Movie Recommendor")
selected_movie_name = st.selectbox(
    'Here are the list of available movies:',movies_df['title'].values
)

if st.button("Recommend"):
    recommended_movie, recommended_movie_poster = recommend(selected_movie_name)

    columns = st.columns(5)
    for i in range(5):
        with columns[i]:
            st.image(recommended_movie_poster[i-1])
            st.text(recommended_movie[i - 1])





