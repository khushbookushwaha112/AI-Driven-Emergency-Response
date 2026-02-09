
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Load trained models
# Ensure these .pkl files are in the same folder as app.py
try:
    model = joblib.load('crime_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    crime_details = joblib.load('crime_details.pkl')
    print("Models and Logic Matrix loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")
    model = None
    vectorizer = None
    crime_details = {}

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>AI Crime Detection API is Running!</h1>"

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not vectorizer:
        return jsonify({'error': 'Model not loaded correctly'}), 500
    
    try:
        data = request.get_json()
        fir_text = data.get('fir_text', '')
        
        if not fir_text:
            return jsonify({'error': 'No FIR text provided'}), 400
        
        # Preprocess text (same as training)
        text_vector = vectorizer.transform([fir_text])
        
        # Predict
        prediction = model.predict(text_vector)[0]
        confidence = model.predict_proba(text_vector).max() * 100
        
        # Get details from the matrix
        details = crime_details.get(prediction, {})
        
        return jsonify({
            'prediction': prediction,
            'confidence': f"{confidence:.2f}%",
            'priority': details.get('Priority', 'Unknown'),
            'action': details.get('Action', 'Standard Protocol'),
            'response_units': details.get('Response_Units', 'Local Police'),
            'input_text': fir_text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
