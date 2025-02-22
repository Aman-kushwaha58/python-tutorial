import flask_

from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Dummy function to simulate product details retrieval.
def get_product_details(product_name):
    # Simulated details for demonstration.
    details = {
        "name": product_name,
        "rating": round(random.uniform(3.0, 5.0), 1),
        "description": f"{product_name} is a popular product known for its quality and reliability."
    }
    return details

# Dummy sentiment analysis function.
def analyze_sentiment(product_name):
    # In a real model, you might load a machine learning model to predict sentiment.
    # Here we simulate by using a simple heuristic:
    simulated_review = "This product is amazing! I really love it."  # Dummy review text
    positive_words = ["amazing", "love", "great", "excellent"]
    negative_words = ["bad", "poor", "disappointing", "terrible"]
    
    score = sum([1 for word in positive_words if word in simulated_review.lower()]) - \
            sum([1 for word in negative_words if word in simulated_review.lower()])
    
    # If score is positive, recommend to buy; otherwise, do not.
    recommendation = "Buy" if score > 0 else "Do Not Buy"
    return recommendation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    product_name = data.get("product_name", "Unknown Product")
    
    product_details = get_product_details(product_name)
    recommendation = analyze_sentiment(product_name)
    
    return jsonify({
        "product_details": product_details,
        "recommendation": recommendation
    })

if __name__ == '__main__':
    # Run in debug mode for development purposes
    app.run(debug=True)
