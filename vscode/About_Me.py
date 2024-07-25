import streamlit as st
import requests as req
import os

st.set_page_config(
    page_title="matthew",
    page_icon="👹",
)

st.sidebar.header("woah theres another page")

st.header("hey fellas im matthew")

'i like video game'

st.write("Current working directory:", os.getcwd())

image_path = "images/game.png"

if os.path.exists(image_path):
    st.image(image_path)
else:
    st.write("Image not found!")

'i like quality music'
r = req.get("https://www.youtube.com/watch?v=4L7u4F4cGY0")
st.video(r.url)

'i like anime'
#st.image("images/onepiece.png")

st.header("I am the fattest man trapped in a skinny body")

#if st.checkbox('duck'):
    #st.image("images/duck.jfif")
