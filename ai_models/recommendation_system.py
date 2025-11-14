import joblib
from surprise import SVD, Dataset

# Example recommendation using collaborative filtering
def recommend(user_data):
    model = joblib.load('models/car_recommendation_model.pkl')
    # Example logic for recommendations
    recommendations = model.predict(user_data)
    return recommendations
