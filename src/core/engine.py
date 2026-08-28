from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI(
    title="Quotex 24/7 REST API",
    description="Enterprise-Grade API & WebSocket Engine by CB Traders BD",
    version="2.5.0"
)

@app.get("/")
def root():
    return {"status": "online", "broker": "Quotex", "docs": "https://api1.api.cbtraderbd.xyz/docs", "developer": "https://t.me/YouKnowWho_am"}

@app.get("/api/live-price")
def get_price(pair: str = "EURUSD_otc"):
    return {"broker": "Quotex", "pair": pair, "price": 1.08455, "payout": "88%", "timestamp": int(time.time())}

@app.get("/api/candles")
def get_candles(pair: str = "EURUSD_otc", count: int = 50):
    return {"broker": "Quotex", "pair": pair, "count": count, "candles": []}
