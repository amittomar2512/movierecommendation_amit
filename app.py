import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/original" + poster_path
    return full_path

def recommend(movie):
        movie_index=movies[movies['title']==movie].index[0]
        distance = similarity[movie_index]
        movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movie=[]
        recommendations_poster=[]
        for i in movie_list:
            # fetch poster from api
            recommendations_poster.append(fetch_poster(movies.iloc[i[0]].id))
            recommended_movie.append(movies.iloc[i[0]].title)
        return recommended_movie,recommendations_poster

with open('movie_dict.pkl','rb') as f:
    movie_list=pickle.load(f)
    movies=pd.DataFrame(movie_list)

with open('similarity.pkl','rb') as f1:
    similarity=pickle.load(f1)


st.header("Movie Recommendation System")
selected_Movie=st.selectbox(
'Select the movie',
movies['title'].values)

if st.button('Recommend'):
    recommended_movie,recommendations_poster=recommend(selected_Movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0])
        st.image(recommendations_poster[0])

    with col2:
        st.text(recommended_movie[1])
        st.image(recommendations_poster[1])

    with col3:
        st.text(recommended_movie[2])
        st.image(recommendations_poster[2])

    with col4:
        st.text(recommended_movie[3])
        st.image(recommendations_poster[3])

    with col5:
        st.text(recommended_movie[4])
        st.image(recommendations_poster[4])















