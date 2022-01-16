import streamlit as st

@st.cache
def conclusion():
    st.title("Conclusions and Recommendations")

    st.write("")
    st.subheader("Conclusion")
    st.write("")
    conclusion = Image.open("Assets\Images\Conclusion.PNG")
    st.image(conclusion)
    
    st.write("")
    st.subheader("Recommendations")
    recommendations = Image.open("Assets\Images\Recommendations.PNG")
    st.image(recommendations)
    
    pass