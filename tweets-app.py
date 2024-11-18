# -*- coding: utf-8 -*-
"""Streamlit Twitter Analysis App"""

import pandas as pd
import plotly.express as px
import streamlit as st

# Load data
tweets_url = 'Tweets.csv'
tweets = pd.read_csv(tweets_url)

# Set up Streamlit layout and title
st.title("Twitter Sentiment Analysis by Airline")


# Pie Chart - Count of Tweets by Sentiment
st.subheader("Count of Tweets by Sentiment")
fig_pie = px.pie(tweets, names='airline_sentiment', title='Count of Tweets by Sentiment')
st.plotly_chart(fig_pie)

# Bar Chart - Count of Tweets by Airline
st.subheader("Count of Tweets by Airline")
airline_counts = tweets['airline'].value_counts()

fig = px.bar(airline_counts,
             x=airline_counts.index,
             y=airline_counts.values,
             labels={ 'x' : 'Airline', 'y': 'Number of Tweets'},
             title='Count of Tweets by Airline')
fig.show()
st.plotly_chart(fig_bar)
