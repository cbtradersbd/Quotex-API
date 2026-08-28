from pydantic import BaseModel

class OrderModel(BaseModel):
    pair: str
    amount: float
    direction: str  # CALL or PUT
    expiry_seconds: int = 60
