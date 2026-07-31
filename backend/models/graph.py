from pydantic import BaseModel


class SupplyChainNode(BaseModel):
    id: str
    label: str
    type: str


class SupplyChainEdge(BaseModel):
    source: str
    target: str
    relation: str