import pandas as pd
import streamlit as st
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

working_df=pd.read_csv("working_df.csv")
cv=CountVectorizer(max_features=5000, stop_words='english')
vectors=cv.fit_transform(working_df['tags']).toarray()

similarity = cosine_similarity(vectors)
list1=[]
def recommend(movie):
    try:
        movie_index = working_df[working_df['title']==movie].index[0]
        distances = similarity[movie_index]
        movies_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

        for i in movies_list:
            list1.append(working_df.iloc[i[0]].title)
        return list1
        
    except:
        return "Movie Not found"

st.title("Movie Recommendation application")
movie = st.selectbox("Select the movie you liked" ,working_df['title'].values)

if st.button("Recommend"):
    recommend(movie)
    for i in list1:
        st.success(i)
    
        