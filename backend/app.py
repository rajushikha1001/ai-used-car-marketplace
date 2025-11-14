from flask import Flask, request, jsonify
from flask_cors import CORS
import car_price_prediction
import car_condition_classifier
import sentiment_analysis
import recommendation_system

app = Flask(__name__)
CORS(app)

@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.json
    predicted_price = car_price_prediction.predict(data)
    return jsonify({"predicted_price": predicted_price})

@app.route('/classify_condition', methods=['POST'])
def classify_condition():
    data = request.json
    condition = car_condition_classifier.predict(data['image'])
    return jsonify({"condition": condition})

@app.route('/sentiment_analysis', methods=['POST'])
def analyze_sentiment():
    data = request.json
    sentiment = sentiment_analysis.analyze(data['review'])
    return jsonify({"sentiment": sentiment})

@app.route('/recommend_car', methods=['GET'])
def recommend_car():
    user_data = request.args
    recommendations = recommendation_system.recommend(user_data)
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
