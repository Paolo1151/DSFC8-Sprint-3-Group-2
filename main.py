import streamlit as st

from st_pages import conclusion, introduction, objective, time_series
from st_pages.recommender import Recommender_Page

import os

def initialize():
    PAGES = [
        'Introduction',
        'Objective',
        'Time Series Analysis and Forecasting',
        'Recommendation Engine',
        'Conclusion and Recommendations'
    ]

    print(os.getcwd())
    print(os.listdir())
    print(os.listdir(os.getcwd() + '/Assets/Images'))

    page = st.sidebar.radio("Page Navigation", PAGES)

    if page == 'Introduction':
        introduction.display()
    elif page == 'Objective':
        objective.display()
    elif page == 'Time Series Analysis and Forecasting':
        time_series.display()
    elif page == 'Recommendation Engine':
        on = Recommender_Page()
        #recommendation_engine.display()
    elif page == 'Conclusion and Recommendations':
        conclusion.display()

if __name__ == "__main__":
    initialize() 
