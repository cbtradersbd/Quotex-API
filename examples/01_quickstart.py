from src.core.client import BrokerApiClient
from src.utils.logger import logger

def main():
    logger.info("Connecting to Quotex Live Stream...")
    client = BrokerApiClient()
    data = client.get_live_price("EURUSD_otc")
    logger.info(f"Connected: {data}")
    logger.info("For full unlocked commercial code, contact Telegram: https://t.me/YouKnowWho_am")

if __name__ == "__main__":
    main()
