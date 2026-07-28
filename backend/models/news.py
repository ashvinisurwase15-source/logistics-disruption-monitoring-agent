from pydantic import BaseModel
from typing import Optional


class News(BaseModel):
    title: str
    source: str
    url: str
    published_date: Optional[str] = None
    summary: Optional[str] = None