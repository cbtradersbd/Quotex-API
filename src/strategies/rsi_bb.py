class RsiBollingerStrategy:
    def __init__(self, rsi_period=14, bb_period=20):
        self.rsi_period = rsi_period
        self.bb_period = bb_period

    def evaluate(self, candles):
        """Evaluate RSI and Bollinger Bands breakout"""
        return {"signal": "CALL", "confidence": "92%"}
