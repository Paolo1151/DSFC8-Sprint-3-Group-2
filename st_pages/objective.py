import streamlit as st
from PIL import Image

import os

def display():
    st.write("")
    st.subheader("OBJECTIVES")
    objectives = Image.open(os.getcwd() + "/Assets/Images/Objectives.png")
    st.image(objectives)

    top_pinoy_rappers = Image.open(os.getcwd() + "/Assets/Images/TopPinoyRappers.png")
    st.image(top_pinoy_rappers)
    
    st.write("")
    st.subheader("METHODOLOGY")
    forecasting = Image.open(os.getcwd() + "/Assets/Images/Method_Forecasting.png")
    st.image(forecasting)

    reco_engine = Image.open(os.getcwd() + "/Assets/Images/Method_RecoEngine.png")
    st.image(reco_engine)