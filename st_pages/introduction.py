import streamlit as st
from PIL import Image

import os

def display():
    st.title("ABRA: The Comeback")
    st.subheader('by Data Science Fellowship Cohort 8 - Sprint 3 - Group 2 (2FUSE)')
    st.write('Paolo, Kui, Ale, Selin, MaCris (mentored by Aaron)')
    
    title_slide = Image.open(os.getcwd() + '/assets/images/TitleSlide.png')
    
    st.write("")
    st.subheader("WHO IS ABRA?")
    st.write("https://abraofficial.com/")
    who = Image.open(os.getcwd() + "/assets/images/IntroAbra.png")
    st.image(who)

    st.write("")
    st.subheader("ABRA'S DISCOGRAPHY")
    discography = Image.open(os.getcwd() + "/assets/images/Discography.png")
    st.image(discography)
    st.markdown("For more Abra's works, go to: https://www.youtube.com/c/abraofficial/featured") 
    st.markdown("Listen to Abra's collaboration with Chito Miranda: https://youtu.be/9QcIo20wok0")