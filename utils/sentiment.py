from textblob import TextBlob

def get_sentiment(text):
    return round(TextBlob(text).sentiment.polarity, 3)
