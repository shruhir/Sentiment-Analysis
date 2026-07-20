## Project Overview
This project demonstrates how to build end-to-end sentiment analysis applications using BERT and Hugging Face Transformers.
It includes multiple deployment approaches:
-Flask Web App with Ngrok tunneling
-FastAPI Service for API-based sentiment prediction
-Dockerized setup for containerized deployment
-The applications allow users to input text and receive sentiment predictions (Positive/Negative), with extensions for emotion classification.

## Objectives
-Fine-tune and use BERT models for sentiment analysis.
-Build interactive Flask and FastAPI applications.
-Deploy models with Ngrok tunneling for public access.
-Containerize the application using Docker for portability.

## Project Structure
sentiment-analysis-project/
│
├── bert-sentiment-app/          # Flask-based app
│   ├── app.py                   # Flask application
│   ├── sentiment_model.py       # BERT model logic
│   └── templates/               # HTML templates
│       ├── index.html           # Input form
│       └── result.html          # Result page
│
├── fastapi-sentiment-app/       # FastAPI-based app
│   ├── main.py                  # FastAPI application
│   ├── sentiment_model.py       # Model logic
│   └── templates/               # HTML templates
│       ├── index.html
│       └── result.html
│
├── sentiment-analysis-pipeline/ # Hugging Face pipeline app
│   ├── app.py                   # Flask app setup
│   ├── pipeline_model.py        # Sentiment + emotion pipeline
│   └── templates/
│       ├── index.html
│       └── result.html
│
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker setup
└── README.md                    # Documentation

## Prerequisites
-Google Colab or local Python environment
-Python 3.9+
-Hugging Face Transformers & Datasets
-Flask / FastAPI / Uvicorn / Pyngrok
-Docker (optional, for container deployment)

## Key Features
-BERT Fine-Tuning: Uses IMDb dataset for training sentiment models.
-Flask App: Interactive web form for text input and sentiment prediction.
-FastAPI Service: REST API endpoints (/predict) for JSON-based predictions.
-Ngrok Integration: Exposes local apps to the internet.
-Dockerized Deployment: Lightweight container setup for portability.
-Extended Pipelines: Emotion classification using DistilRoBERTa.

## How to Run
-Flask App
pip install -r requirements.txt
python app.py
Access via Ngrok public URL.

-FastAPI App
pip install fastapi uvicorn transformers torch pyngrok
uvicorn main:app --reload --port 8000
Access via Ngrok tunnel.

-Docker Deployment
docker build -t sentiment-app .
docker run -p 5000:5000 sentiment-app




































