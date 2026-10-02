from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_class: str = Field(..., description="The predicted insurance premium category", example="medium")
    confidence: float = Field(..., description="The confidence score of the prediction (range 0 to 1)", example=0.85)
    class_probabilities: Dict[str, float] = Field(..., description="Probabilities distribuction across all classes", example={"low": 0.1, "medium": 0.85, "high": 0.05})