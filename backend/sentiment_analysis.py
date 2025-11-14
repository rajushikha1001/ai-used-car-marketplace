from transformers import pipeline

def analyze(review):
    sentiment_pipeline = pipeline('sentiment-analysis')
    result = sentiment_pipeline(review)
    return result[0]['label']
