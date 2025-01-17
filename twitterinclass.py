
import pandas as pd

tweets = pd.read_csv('Tweets.csv')


# prompt: make a pie graph for count of tweets by using plotly . Take count from airline_sentiment

import pandas as pd
import plotly.express as px

# Path for data
# https://raw.githubusercontent.com/Ashok0143/am-tweets/refs/heads/main/Tweets.csv
tweets = pd.read_csv('Tweets.csv')

# Create the pie chart
fig = px.pie(tweets, names='airline_sentiment', title='Count of Tweets by Sentiment')
fig.show()

# prompt: Tweets count by Airline

# Assuming 'tweets' DataFrame is already loaded as in the previous code

# Count of tweets for each airline
airline_counts = tweets['airline'].value_counts()

# Create the bar graph using Plotly
fig = px.bar(airline_counts,
             x=airline_counts.index,
             y=airline_counts.values,
             labels={ 'x' : 'Airline', 'y': 'Number of Tweets'},
             title='Count of Tweets by Airline')
fig.show()

# prompt: Tweets count by Airline

# Assuming 'tweets' DataFrame is already loaded as in the previous code

# Count of tweets for each airline
airline_counts = tweets['airline'].value_counts()

# Create the bar graph using Plotly
fig = px.bar(airline_counts, 
             x=airline_counts.index, 
             y=airline_counts.values,
             labels={ 'x' : 'Airline', 'y': 'Number of Tweets'},
             title='Count of Tweets by Airline')
fig.show()
