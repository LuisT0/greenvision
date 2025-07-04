# app/model.py
import numpy as np
from PIL import Image
import io
import os
import tensorflow as tf

CLASS_NAMES = ['Hazardous', 'Organic', 'Recyclable', 'Non-Recyclable']

def load_model(model_path: str = None):
    if model_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, "..", "models", "greenvision_model")  
    return tf.keras.models.load_model(model_path, compile=False)

def preprocess_image(contents: bytes) -> np.ndarray:
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    img = img.resize((224, 224))
    arr = np.array(img, dtype=np.float32) / 255.0
    return np.expand_dims(arr, axis=0)

