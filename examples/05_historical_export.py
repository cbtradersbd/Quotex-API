from src.services.database import CandleDatabase
from src.utils.logger import logger

def export_data():
    db = CandleDatabase()
    logger.info("Quotex Historical Database initialized for export.")

if __name__ == "__main__":
    export_data()
