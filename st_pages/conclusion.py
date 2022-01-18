import streamlit as st
from PIL import Image

import os

def display():
    st.title("Conclusions and Recommendations")

    st.write("")
    st.subheader("Conclusion")
    st.write("")
    conclusion = Image.open(os.getcwd() + "/Assets/Images/Conclusion.png")
    st.image(conclusion)
    
    st.write("")
    st.subheader("Recommendations")
    recommendations = Image.open(os.getcwd() + "/Assets/Images/Recommendations.png")
    st.image(recommendations)