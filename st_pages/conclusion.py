import streamlit as st
from PIL import Image

import os

def display():
    st.title("Conclusions and Recommendations")

    st.write("")
    st.subheader("Conclusion")
    st.write("")
    conclusion = Image.open(os.getcwd() + "/assets/images/conclusion.png")
    st.image(conclusion)
    
    st.write("")
    st.subheader("Recommendations")
    recommendations = Image.open(os.getcwd() + "/assets/images/recommendations.png")
    st.image(recommendations)