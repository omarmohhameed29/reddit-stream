import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analyze sentiment of a given text using VADER.

    Returns:
        sentiment (str): 'positive', 'neutral', or 'negative'
        score (float): compound sentiment score
    """
    if not text or not isinstance(text, str):
        return 'neutral', 0.0

    scores = sid.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        sentiment = 'positive'
    elif compound <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    return sentiment, compound