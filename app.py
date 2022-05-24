import pickle
import streamlit as st
import pandas as pd
import requests

def get_poster(movie_id):
  url = "https://api.themoviedb.org/3/movie/{}?api_key=5b23ce0eeb95b91e1fae905d65606841&language=en-US".format(movie_id)
  data = requests.get(url)
  data = data.json()
  poster_path = data["poster_path"]
  full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
  return full_path

def recommendation_funtion(movie):
  index = movies[movies["title"] == movie].index[0]
  distances = sorted(list(enumerate(similiarity[index])), reverse=True, key=lambda x: x[1])
  recommended_movies_name = []
  recommended_movies_poster = []

  for i in distances[1:6]:
    movie_id = movies.iloc[i[0]].id
    recommended_movies_poster.append(get_poster(movie_id))
    recommended_movies_name.append(movies.iloc[i[0]].title)
  
  return recommended_movies_name, recommended_movies_poster

st.header("Movie recommendation system")
dict_movies = pickle.load(open("Model's/movie_list.pkl", "rb"))
similiarity = pickle.load(open("Model's/similiarity.pkl", "rb"))
movies = pd.DataFrame((dict_movies))

movie_list = movies["title"].values
select_movies = st.selectbox("Select a movie:", movie_list)

if st.button('Show recommendations:'):
  recommended_movies_name, recommended_movies_poster = recommendation_funtion(select_movies)
  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
    st.text(recommended_movies_name[0])
    st.image(recommended_movies_poster[0])
  with col2:
    st.text(recommended_movies_name[1])
    st.image(recommended_movies_poster[1])
  with col3:
    st.text(recommended_movies_name[2])
    st.image(recommended_movies_poster[2])
  with col4:
    st.text(recommended_movies_name[3])
    st.image(recommended_movies_poster[3])
  with col5:
    st.text(recommended_movies_name[4])
    st.image(recommended_movies_poster[4])

row5_spacer1, row5_1, row5_spacer2 = st.columns((.1, 3.2, .1))

with row5_1:
    st.markdown('___')
    about = st.expander('About/Additional Info')
    with about:
        '''
    A Web App by [Lucas Schimidt](https://linkedin.com/in/lucasschimidtc) [repo](https://github.com/lschimidtc/Content-Based-Movie-Recommendation-System)
        '''
    