from pydantic import BaseModel

class CandleModel(BaseModel):
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float = 0.0
