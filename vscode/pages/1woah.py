import streamlit as st
import requests as req
import os

st.set_page_config(page_title="hey im a page", page_icon="👺")

st.sidebar.header("hey im a page")

st.header('now that you know how great i am...\n\n')

st.subheader("how awesome am i?????")

liker = st.slider('liker') 
if(liker==100):
    st.write("heck yes dude!")
    st.header("👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍")
else:
    st.write("boooooooooooooooooooooooooooooooooo ur wrong")





#9B1CFF
#E9E9E9
#E1CAFF
