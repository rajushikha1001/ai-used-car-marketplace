import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Dataset directory structure MUST be:
# ai_models/dataset/train/<ClassName>/
# ai_models/dataset/validation/<ClassName>/

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
train_dir = os.path.join(BASE_DIR, "dataset/train")
val_dir = os.path.join(BASE_DIR, "dataset/validation")

# Check dataset exists
if not os.path.exists(train_dir):
    raise FileNotFoundError(f"Training folder not found: {train_dir}")

if not os.path.exists(val_dir):
    raise FileNotFoundError(f"Validation folder not found: {val_dir}")

# Preprocessing images
train_datagen = ImageDataGenerator(rescale=1/255)
val_datagen = ImageDataGenerator(rescale=1/255)

train_set = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=16,
    class_mode='categorical'
)

val_set = val_datagen.flow_from_directory(
    val_dir,
    target_size=(224, 224),
    batch_size=16,
    class_mode='categorical'
)

# Simple CNN Model
model = Sequential([
    tf.keras.Input(shape=(224, 224, 3)),
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Flatten(),
    Dense(128, activation='relu'),
    Dense(4, activation='softmax')   # 4 Classes: Poor, Fair, Good, Excellent
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(train_set, validation_data=val_set, epochs=3)

# Save trained model to backend models folder
model_save_path = os.path.join(BASE_DIR, "../backend/models/car_condition_classifier.h5")
model.save(model_save_path)

print(f"Model training complete. Saved to: {model_save_path}")
