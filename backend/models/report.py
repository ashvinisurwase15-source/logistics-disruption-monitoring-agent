from pydantic import BaseModel
from typing import List


class Report(BaseModel):
    generated_at: str
    total_news: int
    high_risk_events: int
    suppliers_impacted: List[str]
    summary: str