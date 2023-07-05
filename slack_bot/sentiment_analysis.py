```python
from textblob import TextBlob

def analyze_sentiment(message):
    """
    Function to analyze the sentiment of a message.
    Uses TextBlob to determine polarity and subjectivity of the message.
    Polarity is a float within the range [-1.0, 1.0] where -1 means negative sentiment and 1 means a positive sentiment.
    Subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
    """
    analysis = TextBlob(message)
    sentiment = analysis.sentiment
    return sentiment
```