import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load the data into a DataFrame
df = pd.read_csv('BA_reviews.csv')

# Sentiment Analysis
def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis to the 'reviews' column
df['Sentiment'] = df['reviews'].apply(get_sentiment)

# Visualize Sentiment Distribution
sentiment_counts = df['Sentiment'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Sentiment Distribution of Reviews')
plt.savefig('visualisation.png')
plt.show()
