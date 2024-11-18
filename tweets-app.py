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

# Display the first few rows of data
st.write("Sample of the Tweet Data:")
st.write(tweets.head())

# Display the dataset shape
st.write("Dataset shape:", tweets.shape)

# Pie Chart - Count of Tweets by Sentiment
st.subheader("Count of Tweets by Sentiment")
fig_pie = px.pie(tweets, names='airline_sentiment', title='Count of Tweets by Sentiment')
st.plotly_chart(fig_pie)

# Bar Chart - Count of Tweets by Airline
st.subheader("Count of Tweets by Airline")
airline_counts = tweets['airline'].value_counts()

# Custom color for each airline (adjust colors as needed)
colors = px.colors.qualitative.Set3  # You can change this to any other color set available in Plotly

fig_bar = px.bar(
    x=airline_counts.index,
    y=airline_counts.values,
    labels={'x': 'Airline', 'y': 'Number of Tweets'},
    title='Count of Tweets by Airline',
    color_discrete_sequence=colors
)
st.plotly_chart(fig_bar)
