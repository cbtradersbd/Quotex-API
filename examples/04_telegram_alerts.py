from src.services.telegram_bot import TelegramService

def send_alert():
    service = TelegramService()
    service.send_signal({"pair": "EURUSD_otc", "direction": "CALL (BUY)", "winrate": "92%"})

if __name__ == "__main__":
    send_alert()
