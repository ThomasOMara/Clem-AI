from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from globals import text_queue
from globals import sentiment_queue

def get_sentiment_data():

    sentiment_analyser = SentimentIntensityAnalyzer()

    print("Starting sentiment thread")

    while True:
        if not text_queue.empty():
            sentence = text_queue.get()
            sentiment_data = sentiment_analyser.polarity_scores(sentence)
            sentiment_queue.put(sentiment_data)
