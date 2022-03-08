import pandas as pd
import streamlit as st


import get_data as data

st.set_page_config(page_title="WebScrapping - PY101", page_icon="🛒", layout="wide")
st.image("https://unpackai.github.io/unpackai_logo.svg")
st.title("WebScrapping of Lego Prices around the world 🌏")
st.write("*by <name>*")
# st.write("---")
number_of_students = st.slider("Number of students in the class", 1, 35)
st.write("There are ",number_of_students," students in the class")
