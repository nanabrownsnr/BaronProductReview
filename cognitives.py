from transformers import pipeline
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import numpy as np
import json

def load_models():
    model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path, trust_remote_code=True)
    sentiment_classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
 
    category_classifier = pipeline("zero-shot-classification", model="MoritzLaurer/deberta-v3-large-zeroshot-v2.0")

    return sentiment_classifier,category_classifier


sentiment_classifier,category_classifier = load_models()


def determine_sentiment(text):
    try:
        response = sentiment_classifier(text)
        if response and len(response) > 0 and len(response[0]) > 0:
            result = response[0]['label']
            # print("sentiment result:", result)
        else:
            raise ValueError("Invalid JSON response format")
    except (json.JSONDecodeError, IndexError, KeyError, ValueError) as e:
        print(f"Error processing emotion: {e}")
        result = "Failed"
    return result

def determine_category(text,categories):
    try:
        response = category_classifier(text,categories)
        if response and len(response) > 0:
            result = response['labels'][0]
            # print("category result:", result)
        else:
            raise ValueError("Invalid JSON response format")
    except (json.JSONDecodeError, IndexError, KeyError, ValueError) as e:
        print(f"Error processing emotion: {e}")
        result = "Failed"
    return result
