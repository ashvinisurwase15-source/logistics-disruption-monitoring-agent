from pydantic import BaseModel


class RiskAssessment(BaseModel):
    title: str
    severity: str
    category: str
    region: str
    confidence: float
    reason: str