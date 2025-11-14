import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import joblib
import os

MODEL_PATH = "models/car_price_predictor.pkl"

# Train only when model does NOT exist
if not os.path.exists(MODEL_PATH):
    print("Training car price prediction model...")

    # Load dataset
    df = pd.read_csv("used_cars_data.csv")

    # Feature columns
    feature_cols = ['make', 'model', 'year', 'mileage', 'condition', 'location']
    X = df[feature_cols]
    y = df['price']

    # Categorical & numeric fields
    categorical_features = ['make', 'model', 'condition', 'location']
    numeric_features = ['year', 'mileage']

    # Preprocessor (OneHotEncoding categorical columns)
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
            ('num', 'passthrough', numeric_features)
        ]
    )

    # Build full training pipeline
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=200, random_state=42))
    ])

    # Train model
    model.fit(X, y)

    # Save model
    joblib.dump(model, MODEL_PATH)
    print("Model training completed and saved.")

else:
    print("Model already exists. Skipping training.")

# --------------------
# Predict function
# --------------------
def predict(data):
    model = joblib.load(MODEL_PATH)

    # Convert input to DataFrame
    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]
    return float(prediction)
