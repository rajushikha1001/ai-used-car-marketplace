import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

MODEL_PATH = "models/car_condition_classifier.h5"

# Load model once
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Train it first.")

model = load_model(MODEL_PATH)

# Class labels in order (edit if needed)
CLASS_NAMES = ["Poor", "Fair", "Good", "Excellent"]

def predict(image_path):
    try:
        # Load and preprocess image
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        preds = model.predict(img_array)
        class_index = np.argmax(preds)

        return CLASS_NAMES[class_index]

    except Exception as e:
        return f"Error processing image: {str(e)}"
