import streamlit as st

from pages import conclusion, introduction, objective, recommendation_engine, time_series

def initialize():
    PAGES = [
        'Introduction',
        'Objective',
        'Time Series Analysis and Forecasting',
        'Recommendation Engine',
        'Conclusion and Recommendations'
    ]

    page = st.sidebar.radio("Page Navigation", PAGES)

    if page == 'Introduction':
        introduction.display()
    elif page == 'Objective':
        objective.display()
    elif page == 'Time Series Analysis and Forecasting':
        time_series.display()
    elif page == 'Recommendation Engine':
        recommendation_engine.display()
    elif page == 'Conclusion and Recommendations':
        conclusion.display()

if __name__ == "__main__":
    initialize() 