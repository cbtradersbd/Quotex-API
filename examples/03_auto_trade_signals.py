from src.strategies.rsi_bb import RsiBollingerStrategy
from src.utils.logger import logger

def run_strategy():
    strat = RsiBollingerStrategy()
    result = strat.evaluate([])
    logger.info(f"Quotex AI Strategy Evaluation: {result}")

if __name__ == "__main__":
    run_strategy()
