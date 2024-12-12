import pandas
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("John Doe")
    content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sollicitudin dui eget augue interdum viverra. Mauris a placerat sem. Cras fermentum nisl sit amet ex tempor facilisis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam sit amet diam odio. Morbi ipsum sapien, cursus lobortis feugiat nec, consectetur a lorem. Vivamus blandit placerat risus, sit amet venenatis ex interdum sed. Fusce venenatis est vitae tellus efficitur pulvinar. Aenean pretium feugiat magna, in elementum libero laoreet in. Vivamus in faucibus libero, in volutpat turpis."""
    st.info(content)
st.write("Below you can find some of the apps I have built in Python. Fell free to contact me!")

df = pandas.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])