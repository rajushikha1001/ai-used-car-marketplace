import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset (e.g., from CSV or external source)
df = pd.read_csv('used_cars_data.csv')

# Features and target variable
features = ['make', 'model', 'year', 'mileage', 'condition']
X = df[features]
y = df['price']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'models/car_price_predictor.pkl')
