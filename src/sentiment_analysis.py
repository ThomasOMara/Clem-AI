'''
Analyse text to determine sentiment.

The level of "negative" sentiment is based on the compound score returned from VADER.

https://github.com/cjhutto/vaderSentiment

The compound score is computed by summing the valence scores of each word in the lexicon,
adjusted according to the rules, and then normalized to be between -1 (most extreme negative)
and +1 (most extreme positive). This is the most useful metric if you want a single unidimensional
measure of sentiment for a given sentence.
Calling it a 'normalized, weighted composite score' is accurate.

It is also useful for researchers who would like to set standardized thresholds for classifying
sentences as either positive, neutral, or negative. Typical threshold values ... are:
* positive sentiment: compound score >= 0.05
* neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
* negative sentiment: compound score <= -0.05
'''

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
