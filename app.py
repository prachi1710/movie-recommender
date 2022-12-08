import streamlit as st
import pickle
import pandas as pd
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

def recommend(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distances=similarity[movie_index]
  movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

  recommended_movies=[]


  for i in movie_list:
    recommended_movies.append(movies.iloc[i[0]].title)
  return recommended_movies


st.title('Movie Recommender System')
Selected_movie_name=st.selectbox(
'Search your movies', movies['title'].values
)

similarity=pickle.load(open('similarity.pkl','rb'))
if st.button('Recommend'):
    recommendations=recommend(Selected_movie_name)
    for i in recommendations:
        st.write(i)

