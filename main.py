import streamlit as st

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
