import streamlit as st
from PIL import Image

import os

def display():
    st.title("ABRA: The Comeback")
    st.subheader('by Data Science Fellowship Cohort 8 - Sprint 3 - Group 2 (2FUSE)')
    st.write('Paolo, Kui, Ale, Selin, MaCris (mentored by Aaron)')
    
    title_slide = Image.open(os.getcwd() + '/Assets/Images/TitleSlide.png')
    
    print(os.getcwd())
    print(os.listdir())
    print(os.listdir(os.getcwd() + '/Assets'))

    st.write("")
    st.subheader("WHO IS ABRA?")
    st.write("https://abraofficial.com/")
    who = Image.open(os.getcwd() + "/Assets/Images/IntroAbra.png")
    st.image(who)

    st.write("")
    st.subheader("ABRA'S DISCOGRAPHY")
    discography = Image.open(os.getcwd() + "/Assets/Images/Discography.png")
    st.image(discography)
    st.markdown("For more Abra's works, go to: https://www.youtube.com/c/abraofficial/featured") 
    st.markdown("Listen to Abra's collaboration with Chito Miranda: https://youtu.be/9QcIo20wok0")