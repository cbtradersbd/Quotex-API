# ⚡ Quotex 24/7 Live REST API, WebSocket Streamer & AI Signal Engine

> **⚡ Enterprise-Grade 24/7 Self-Healing REST API & WebSocket wrapper for Quotex (Real & OTC asset pairs). Live M1 candle history, live payouts & trading bot engine.**

[![Official Telegram Channel](https://img.shields.io/badge/Official_Telegram-CB_Traders_BD-2CA5E0?style=for-the-badge&logo=telegram)](https://t.me/+R_kEsY9yqkA1NDI1)
[![Direct Contact](https://img.shields.io/badge/Chat_on_Telegram-@YouKnowWho__am-blue?style=for-the-badge&logo=telegram)](https://t.me/YouKnowWho_am)
[![AI Signals Bot Demo](https://img.shields.io/badge/Live_Signals_Bot-@cbsignalsproai__bot-red?style=for-the-badge&logo=telegram)](https://t.me/cbsignalsproai_bot?start=1)
[![Account Verify Bot](https://img.shields.io/badge/Account_Verify_Bot-@cbtradersbd__bot-purple?style=for-the-badge&logo=telegram)](https://t.me/cbtradersbd_bot?start=1)
[![FastAPI Swagger Docs](https://img.shields.io/badge/Live_API-FastAPI_Swagger-009688?style=for-the-badge&logo=fastapi)](https://api1.api.cbtraderbd.xyz/docs)
[![Python Version](https://img.shields.io/badge/Python-3.10_|_3.11_|_3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://api1.api.cbtraderbd.xyz/docs)
[![Docker Support](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://api1.api.cbtraderbd.xyz/docs)
[![License](https://img.shields.io/badge/License-Commercial_Source_Code-emerald?style=for-the-badge)](https://t.me/YouKnowWho_am)

---

## 📑 Table of Contents
1. [🌟 System Overview & Highlights](#-system-overview--highlights)
2. [🚀 Live API Interactive Swagger Documentation](#-live-api-interactive-swagger-documentation)
3. [🤖 Official Telegram Bots & Live Demos](#-official-telegram-bots--live-demos)
4. [🏗️ Architectural Design & Protocol Mechanics](#️-architectural-design--protocol-mechanics)
5. [📦 Complete Project Directory Structure](#-complete-project-directory-structure)
6. [⚡ Fast Installation & 1-Click Deployment](#-fast-installation--1-click-deployment)
7. [⚙️ Configuration Parameters (.env & JSON)](#️-configuration-parameters-env--json)
8. [💻 Code Examples & Integration Snippets](#-code-examples--integration-snippets)
9. [📡 Available REST Endpoints & WebSocket Feeds](#-available-rest-endpoints--websocket-feeds)
10. [🎯 Signal Engine, Indicators & Winrate Filter](#-signal-engine-indicators--winrate-filter)
11. [🛡️ Self-Healing, Cloudflare Bypass & Anti-Ban Architecture](#️-self-healing-cloudflare-bypass--anti-ban-architecture)
12. [🛒 Commercial Source Code Purchase & Licensing](#-commercial-source-code-purchase--licensing)
13. [💬 Direct Contact & Community](#-direct-contact--community)

---

## 🌟 System Overview & Highlights
**Quotex 24/7 Live REST API, WebSocket Streamer & AI Signal Engine** is a state-of-the-art, enterprise-grade Python FastAPI REST and WebSocket protocol wrapper engineered specifically for **Quotex**. Built for algorithmic traders, prop trading firms, signal providers, and quantitative developers requiring 24/7 ultra-low latency execution and non-repainting market data streams.

- 🕒 **24/7 Real & OTC Market Feeds**: Continuous live data streams 365 days a year.
- 📊 **8-Day M1 Rolling Candle History**: Zero-repaint database records.
- 💰 **Real-Time Payout Tracking**: Accurate percentage recorded per minute.
- 🛡️ **Bulletproof Self-Healing**: Auto-reconnect & Cloudflare session manager.

---

## 🚀 Live API Interactive Swagger Documentation
Experience the live production API server, test interactive Swagger requests, and inspect real-time schemas directly in your browser:  
👉 **[https://api1.api.cbtraderbd.xyz/docs](https://api1.api.cbtraderbd.xyz/docs)**

---

## 🤖 Official Telegram Bots & Live Demos
You can immediately test our algorithms and automated account systems on Telegram:
* 🎯 **AI Trading Signals Bot (90%+ Accuracy):** Instant multi-broker signals:  
  👉 **[https://t.me/cbsignalsproai_bot?start=1](https://t.me/cbsignalsproai_bot?start=1)**
* 🛡️ **Affiliate ID Account Verification Bot:** Verify trader UID & active status:  
  👉 **[https://t.me/cbtradersbd_bot?start=1](https://t.me/cbtradersbd_bot?start=1)**
* 📢 **Official Telegram Channel:** Market updates, bot releases & live signals:  
  👉 **[https://t.me/+R_kEsY9yqkA1NDI1](https://t.me/+R_kEsY9yqkA1NDI1)**

---

## 🏗️ Architectural Design & Protocol Mechanics

```
┌────────────────────────────────────────────────────────┐
│                   CB TRADERS BD GATEWAY                │
│       https://api1.api.cbtraderbd.xyz/docs             │
└──────────────┬──────────────────────────┬──────────────┘
               │                          │
       REST API Requests          WebSocket Stream (WSS)
               │                          │
┌──────────────▼──────────────┐   ┌───────▼──────────────────────┐
│  FastAPI Async Web Server   │   │  High-Speed WebSocket Pool   │
│  - Endpoint Validation      │   │  - Binary Frame Parsing      │
│  - JSON Schema Serializer   │   │  - Heartbeat Keep-Alive      │
│  - Token Authentication     │   │  - Auto-Reconnect Daemon     │
└──────────────┬──────────────┘   └───────┬──────────────────────┘
               │                          │
┌──────────────▼──────────────────────────▼──────────────┐
│                  Core Engine Layer                     │
│  - Session Manager & Cloudflare Clearance Handler      │
│  - Non-Repaint M1/M5 Historical Candle Persistence     │
│  - AI Multi-Indicator Signal Strategy Pipeline         │
└──────────────────────────────┬─────────────────────────┘
                               │
               ┌───────────────▼───────────────┐
               │    Quotex Live Platform    │
               │   (Real Markets & 24/7 OTC)   │
               └───────────────────────────────┘
```

---

## 📦 Complete Project Directory Structure
This repository features an expansive, clean, and production-ready modular architecture:

```
├── config/
│   ├── default.json             # Server host, port & connection pool configuration
│   └── strategies.json          # Technical indicators, RSI thresholds & Martingale setups
├── docs/
│   ├── API_REFERENCE.md         # Exhaustive endpoint reference and request/response payloads
│   └── DEPLOYMENT_GUIDE.md      # Step-by-step VPS Linux (Ubuntu/Debian) & Docker setup
├── examples/
│   ├── 01_quickstart.py         # 1-Click connection and live price check
│   ├── 02_stream_candles.py     # Real-time WebSocket tick and candlestick listener
│   ├── 03_auto_trade_signals.py # Automated execution based on AI indicator signals
│   ├── 04_telegram_alerts.py    # Formatting and broadcasting signals to Telegram channels
│   └── 05_historical_export.py  # Exporting multi-day M1/M5 datasets to CSV and SQLite
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── auth.py              # Cloudflare session token & cookie rotation manager
│   │   ├── client.py            # High-throughput asynchronous HTTP/REST client
│   │   ├── engine.py            # Master order processing & market event pipeline
│   │   └── websocket.py         # Resilient WebSocket protocol frame parser
│   ├── models/
│   │   ├── __init__.py
│   │   ├── candle.py            # Pydantic OHLCV candle validation schemas
│   │   ├── order.py             # Binary options trade order payload models
│   │   └── payout.py            # Live asset payout percentage schema
│   ├── services/
│   │   ├── __init__.py
│   │   ├── database.py          # SQLite/PostgreSQL persistence for 8-day rolling candles
│   │   └── telegram_bot.py      # Async Telegram broadcast & notification engine
│   ├── strategies/
│   │   ├── __init__.py
│   │   ├── martingale.py        # Dynamic stake sizing & risk mitigation calculator
│   │   ├── price_action.py      # Support/Resistance, Pinbar & Engulfing pattern scanner
│   │   └── rsi_bb.py            # RSI (14) + Bollinger Bands (20, 2) breakout analyzer
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py           # Timezone converters, timestamp formatters & math tools
│       └── logger.py            # Colored asynchronous console & file logger
├── scripts/
│   ├── install.sh               # Automated Linux dependency installer
│   └── start_api.bat            # 1-Click Windows production launcher
├── .env.example                 # Environment variables template
├── .gitignore                   # Standard Python git exclusions
├── Dockerfile                   # Multi-stage optimized Docker build
├── docker-compose.yml           # Complete containerized service stack
├── requirements.txt             # Locked production dependencies
└── README.md                    # In-depth system documentation
```

---

## ⚡ Fast Installation & 1-Click Deployment

### Option A: Local Python Environment
```bash
# 1. Clone the repository
git clone https://github.com/cbtradersbd/quotex-api.git
cd quotex-api

# 2. Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# 3. Install required production dependencies
pip install -r requirements.txt

# 4. Configure your environment
cp .env.example .env

# 5. Launch the FastAPI server
python -m uvicorn src.core.engine:app --host 0.0.0.0 --port 8000 --reload
```

### Option B: Docker Containerization
```bash
docker-compose up -d --build
```

---

## ⚙️ Configuration Parameters (.env & JSON)

```ini
# .env Configuration File
API_BASE_URL=https://api1.api.cbtraderbd.xyz
API_KEY=cb_traders_bd_license_unlocked
BROKER=quotex
DEFAULT_TIMEFRAME=1m
RETENTION_DAYS=8
TIMEZONE_OFFSET=UTC+6
LOG_LEVEL=INFO
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=@your_channel
```

---

## 💻 Code Examples & Integration Snippets

### 1. Fetch Live Price & Continuous 24/7 OTC Feed
```python
from src.core.client import BrokerApiClient
from src.utils.logger import logger

client = BrokerApiClient(base_url="https://api1.api.cbtraderbd.xyz/docs")
price_data = client.get_live_price("EURUSD_otc")
logger.info(f"Live Tick: {price_data}")
```

### 2. Stream Real-Time Candlesticks via WebSocket
```python
import asyncio
from src.core.websocket import ResilientWebSocketClient
from src.utils.logger import logger

async def on_candle(candle):
    logger.info(f"Closed M1 Candle: Time={candle.time}, Open={candle.open}, High={candle.high}, Low={candle.low}, Close={candle.close}")

async def main():
    ws = ResilientWebSocketClient(pair="EURUSD_otc")
    await ws.connect_and_listen(callback=on_candle)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 📡 Available REST Endpoints & WebSocket Feeds

| Endpoint | Method | Purpose | Response Format |
| :--- | :---: | :--- | :--- |
| `/docs` | `GET` | Interactive Swagger API Explorer | HTML / UI |
| `/api/quotex/live-price` | `GET` | Current bid/ask and tick stream | JSON |
| `/api/quotex/candles` | `GET` | Historical closed OHLCV candle records | JSON Array |
| `/api/quotex/payouts` | `GET` | Live payout percentage monitor for all pairs | JSON Object |
| `/api/quotex/signals` | `POST` | Execute automated strategy webhook trigger | JSON Result |
| `/ws/quotex/stream` | `WSS` | Ultra-low latency binary WebSocket feed | Binary / JSON |

---

## 🎯 Signal Engine, Indicators & Winrate Filter
* **Non-Repainting Guarantee:** Signals are calculated strictly on closed candles ($T-1$). Running ticks are never used for candle finalization.
* **Triple Confirmation Filter:**
  1. **RSI Divergence:** 14-period Relative Strength Index overbought ($>70$) and oversold ($<30$) boundary detection.
  2. **Bollinger Band Squeeze:** 20-period moving average with 2.0 standard deviation breakout validation.
  3. **Trend Matrix:** Exponential Moving Average (EMA 50 / EMA 200) trend directional filter.
* **Integrated Martingale Calculator:** Auto-calculates step 1 & step 2 recovery stakes based on live asset payout rates.

---

## 🛡️ Self-Healing, Cloudflare Bypass & Anti-Ban Architecture
* **Zero-Drop Resilience:** Automatically reconnects upon network interruptions with exponential backoff.
* **Token Clearance Handler:** Bypasses Cloudflare Turnstile and session expirations seamlessly in the background.
* **Downtime Gap Recovery:** Detects offline intervals and automatically queries past candles to backfill missing database records.

---

## 🛒 Commercial Source Code Purchase & Licensing

Looking for the 100% full, unlocked source code with complete ownership, personal API keys, or custom bot development?

### Full Commercial Package Includes:
* 📦 **100% Full Unlocked Source Code** (`app.py`, WebSocket protocols, database engine, AI signal bots).
* 🚀 **1-Click Automated Launchers** for Windows, Linux VPS, and Docker.
* ⚡ **Unlimited Deployments** on unlimited servers with zero restrictions.
* 🛠️ **24/7 1-on-1 Developer Setup Assistance & Support**.
* 🔄 **Lifetime Code Updates & Strategy Enhancements**.

### 💳 Accepted Payment Methods:
* USDT (TRC20 / BEP20)
* Binance Pay (UID / Pay ID)
* Bitcoin / Ethereum / Crypto
* Local Mobile Banking & Wire Transfers

---

## 💬 Direct Contact & Community
* 📩 **Direct Telegram (Developer):** [@YouKnowWho_am](https://t.me/YouKnowWho_am)
* 📢 **Official Telegram Channel:** [CB Traders BD Official](https://t.me/+R_kEsY9yqkA1NDI1)
* 🤖 **AI Signal Bot Demo:** [@cbsignalsproai_bot](https://t.me/cbsignalsproai_bot?start=1)
* 🛡️ **Account Verify Bot:** [@cbtradersbd_bot](https://t.me/cbtradersbd_bot?start=1)
