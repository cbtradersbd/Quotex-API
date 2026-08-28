# Async Telegram Notification Service
import requests

class TelegramService:
    def __init__(self, bot_token=None, chat_id=None):
        self.bot_token = bot_token
        self.chat_id = chat_id

    def send_signal(self, signal_data):
        message = f"🚀 [Quotex AI SIGNAL]\nPair: {signal_data['pair']}\nDirection: {signal_data['direction']}\nWinrate: {signal_data.get('winrate', '91%')}"
        print("Dispatching Telegram Alert:", message)
