from pydantic import BaseModel

class PayoutModel(BaseModel):
    pair: str
    payout_percentage: int
    is_active: bool
