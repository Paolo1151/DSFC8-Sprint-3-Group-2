import streamlit as st

import pages

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
        pages.introduction.introduction()
    elif page == 'Objective':
        pages.objective.objective()
    elif page == 'Time Series Analysis and Forecasting':
        pages.time_series.time_series()
    elif page == 'Recommendation Engine':
        pages.recommendation_engine.recommendation_engine()
    elif page == 'Conclusion and Recommendations':
        pages.conclusion.conclusion()

if __name__ == "__main__":
    initialize() 