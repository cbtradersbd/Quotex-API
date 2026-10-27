import asyncio
from src.core.binary protocol stream import ResilientBinary Protocol StreamClient
from src.utils.logger import logger

async def on_candle(candle):
    logger.info(f"Live M1 Candle Received: {candle}")

async def main():
    ws = ResilientBinary Protocol StreamClient(pair="EURUSD_otc")
    await ws.connect_and_listen(callback=on_candle)

if __name__ == "__main__":
    asyncio.run(main())
