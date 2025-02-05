import streamlit as st
import requests as req
import os

def get_image_path(image_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "images", image_name)

st.set_page_config(
    page_title="matthew",
    page_icon="👹",
)


#arrow_path = get_image_path("ARROW.webp")

#if os.path.exists(arrow_path):
   # st.sidebar.markdown("arrow_path)
#else:
   # st.write("Image not found!")
st.sidebar.markdown("![Alt Text](https://cdn.pixabay.com/animation/2022/08/13/01/09/01-09-03-923_512.gif)")
st.sidebar.header("woah theres another page")

st.header("hey fellas im matthew")

'i like video game'
game_path = get_image_path("game.png")

if os.path.exists(game_path):
    st.image(game_path)
else:
    st.write("Image not found!")

'i like quality music'
r = req.get("https://www.youtube.com/watch?v=4L7u4F4cGY0")
st.video(r.url)

'i like anime'
op_path = get_image_path("onepiece.png")

if os.path.exists(op_path):
    st.image(op_path)
else:
    st.write("Image not found!")
#st.image("images/onepiece.png")

st.header("I am the fattest man trapped in a skinny body")

if st.checkbox('duck'):
    duck_path = get_image_path("duck.jfif")
    if os.path.exists(duck_path):
        st.image(duck_path)
    else:
        st.write("Image not found!")
