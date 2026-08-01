from pydantic import BaseModel


class SupplierImpact(BaseModel):
    supplier: str
    material: str
    region: str
    impact_level: str
    reason: str