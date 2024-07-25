import streamlit as st
import requests as req
import os

def get_image_path(image_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "./images", image_name)

st.set_page_config(page_title="hey im a page", page_icon="👺")

st.sidebar.header("hey im a page")

st.header('now that you know how great i am...\n\n')

st.subheader("how awesome am i?????")

liker = st.slider('liker') 
if(liker==100):
    st.write("heck yes dude!")
    yes_path = get_image_path("heckyes.jfif")

    if os.path.exists(yes_path):
        st.image(yes_path)
    else:
        st.write("Image not found!")
else:
    st.write("no")





#9B1CFF
#E9E9E9
#E1CAFF
