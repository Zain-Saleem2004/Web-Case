import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/me11.jpg",)

with col2:
    st.title("Zain Abu Saleem")
    content = """
    Hi, I'm Zain! A computer software engineer and a programmer. I am working with my team.
    specialized with PHP Laravel and python.    
    """
    st.info(content)

content2 = """Below you can find some of the apps 
    I have built. Feel free to contact me."""
st.info(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
