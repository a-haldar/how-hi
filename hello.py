from flask import Flask, redirect, url_for, request
import nltk

nltk.download("vader_lexicon")
nltk.download("punkt")
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import json
import pandas as pd
app = Flask(__name__)

sid = SentimentIntensityAnalyzer()

def get_sentiment(text):
    """
    Returns the maximum scoring sentiment of the text

    Parameters:
    ------
    text: (str)
    the input text

    Returns:
    -------
    sentiment of the text: (str)
    """
    scores = sid.polarity_scores(text)
    return max(scores, key=lambda x: scores[x])
    
@app.route('/funapp/api/v1/sentiment',methods = ['GET'])
def process():
    text = request.args.get('text')
    
    #return json.dumps(conv)
    return json.dumps(get_sentiment(text));
@app.route('/test',methods = ['GET'])
def test():
    return '1'

if __name__ == '__main__':
   app.run()


    
