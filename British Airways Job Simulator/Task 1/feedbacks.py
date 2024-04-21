import pandas as pd
from textblob import TextBlob

# Load the data into a DataFrame
df = pd.read_csv('BA_reviews.csv')

# Sentiment Analysis
def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

# Apply sentiment analysis to the 'reviews' column
df['Sentiment'] = df['reviews'].apply(get_sentiment)

# Select top positive feedbacks (assuming positive sentiment > 0.5)
top_feedbacks = df[df['Sentiment'] > 0.5].nlargest(10, 'Sentiment')
#Print top feedbacks
top_feedbacks.to_csv('top_positive_feedbacks.csv', index=False)
# Display or save the top feedbacks
print(top_feedbacks)
