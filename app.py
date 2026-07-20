# # app.py
# from flask import Flask, request, render_template
# from sentiment_model import predict_sentiment

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     text = request.form['text']
#     result = predict_sentiment(text)
#     return render_template('result.html', text=text, result=result)

# if __name__ == '__main__':
#     app.run(debug=True)

# app.py
from flask import Flask, request, render_template
from sentiment_model import predict_sentiment, predict_emotion

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    
    # Fetch sentiment and emotion results with default values if None
    sentiment_result = predict_sentiment(text) or {'label': 'Unknown', 'score': 0}
    emotion_result = predict_emotion(text) or {'label': 'Unknown', 'score': 0}
    
    return render_template('result.html', text=text, sentiment_result=sentiment_result, emotion_result=emotion_result)

if __name__ == '__main__':
    app.run(debug=True)
