# Trading Bot (Binance Futures Testnet)
## Setup
```bash
pip install -r requirements.txt
Binance Futures Testnet Trading Bot

Overview

This project is a simplified trading bot built using Python for Binance Futures Testnet (USDT-M).

Features

- Market Order Support
- Limit Order Support
- BUY and SELL Orders
- Command Line Interface (CLI)
- Input Validation
- Logging
- Error Handling

Installation

Install dependencies:

pip install -r requirements.txt

Environment Variables

Create a ".env" file:

API_KEY=your_api_key

API_SECRET=your_api_secret

Usage

Market Buy:

python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01

Market Sell:

python main.py --symbol BTCUSDT --side SELL --type MARKET --qty 0.01

Limit Buy:

python main.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.01 --limit 50000

Project Structure

- main.py
- orders.py
- requirements.txt
- README.md
- bot/client.py
- bot/validators.py
- bot/logging_config.py

Logging

Logs are stored in "bot.log".

Assumptions

- Binance Futures Testnet account is active.
- Valid API credentials are configured.
- Orders are executed on Binance Futures Testnet only.