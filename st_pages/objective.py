import streamlit as st
from PIL import Image

def display():
    st.write("")
    st.subheader("OBJECTIVES")
    objectives = Image.open("Assets\Images\Objectives.png")
    st.image(objectives)

    top_pinoy_rappers = Image.open("Assets\Images\TopPinoyRappers.png")
    st.image(top_pinoy_rappers)
    
    st.write("")
    st.subheader("METHODOLOGY")
    forecasting = Image.open("Assets\Images\Method_Forecasting.png")
    st.image(forecasting)

    reco_engine = Image.open("Assets\Images\Method_RecoEngine.png")
    st.image(reco_engine)