import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


class NLPProcessor:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))

    def parse_user_input(self, user_input):
        tokenized = sent_tokenize(user_input)
        for i in tokenized:
            words = nltk.word_tokenize(i)
            words = [word for word in words if word.isalnum()]
            words = [word for word in words if word not in self.stop_words]
        return words
