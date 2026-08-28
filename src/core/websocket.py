import asyncio
import json
import time

class ResilientWebSocketClient:
    def __init__(self, pair="EURUSD_otc"):
        self.pair = pair
        self.is_connected = False

    async def connect_and_listen(self, callback=None):
        """Simulate resilient WebSocket frame stream"""
        self.is_connected = True
        print(f"[*] WebSocket connected to Quotex stream for {self.pair}...")
        for _ in range(3):
            candle = {"time": int(time.time()), "pair": self.pair, "open": 1.08420, "high": 1.08465, "low": 1.08410, "close": 1.08455}
            if callback:
                await callback(candle)
            await asyncio.sleep(1)
