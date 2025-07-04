# app/main.py
import os
import logging
from fastapi import FastAPI, UploadFile, File
from app.model import preprocess_image, CLASS_NAMES, load_model 

# Configura logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    try:
        logger.info("📦 Cargando modelo...")
        
        app.state.model = load_model()  
        logger.info("✅ Modelo cargado correctamente")
    except Exception as e:
        logger.error(f"Error cargando el modelo: {e}")
        raise

@app.get("/")
async def read_root():
    return {"message": "GreenVision API en marcha"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        img = preprocess_image(contents)
        preds = app.state.model.predict(img)
        return {"predictions": preds.tolist(), "labels": CLASS_NAMES}
    except Exception as e:
        logger.error(f"Error en predicción: {e}")
        raise