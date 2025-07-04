class PredictResponse(BaseModel):
    label: str = Field(..., description="Etiqueta que predijo el modelo")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confianza de la predicción (entre 0 y 1)")

    class Config:
        schema_extra = {
            "example": {
                "label": "Recyclable",
                "confidence": 0.87
            }
        }

class FeedbackRequest(BaseModel):
    predicted: str = Field(..., description="Etiqueta que el modelo entregó")
    correct: str = Field(..., description="Etiqueta correcta según el usuario")

    class Config:
        schema_extra = {
            "example": {
                "predicted": "Organic",
                "correct": "Hazardous"
            }
        }