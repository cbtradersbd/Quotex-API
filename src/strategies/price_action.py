class PriceActionStrategy:
    def detect_pinbar(self, open_p, high_p, low_p, close_p):
        """Detect bullish/bearish rejection pinbars"""
        body = abs(close_p - open_p)
        total_range = high_p - low_p
        return body <= total_range * 0.3
