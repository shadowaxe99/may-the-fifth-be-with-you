```python
import unittest
from slack_bot.sentiment_analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):

    def setUp(self):
        self.positive_message = "I love America and the 4th of July celebrations were amazing!"
        self.negative_message = "I didn't enjoy the 4th of July, it was too loud and crowded."

    def test_analyze_sentiment_positive(self):
        sentiment = analyze_sentiment(self.positive_message)
        self.assertGreater(sentiment, 0.5)

    def test_analyze_sentiment_negative(self):
        sentiment = analyze_sentiment(self.negative_message)
        self.assertLess(sentiment, 0.5)

if __name__ == '__main__':
    unittest.main()
```