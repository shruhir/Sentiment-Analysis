# # sentiment_model.py
# from transformers import pipeline

# # Load pre-trained sentiment-analysis pipeline
# nlp = pipeline('sentiment-analysis')

# def predict_sentiment(text):
#     result = nlp(text)[0]
#     return result



# sentiment_model.py
from transformers import pipeline

# Load pre-trained pipelines
sentiment_nlp = pipeline('sentiment-analysis')
emotion_nlp = pipeline('text-classification', model="j-hartmann/emotion-english-distilroberta-base")

def predict_sentiment(text):
    result = sentiment_nlp(text)[0]
    return result

def predict_emotion(text):
    result = emotion_nlp(text)[0]
    return result
