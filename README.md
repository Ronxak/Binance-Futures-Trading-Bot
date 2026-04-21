# Binance Futures Testnet Trading Bot

A simplified, robust Python trading bot designed to place MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M) using direct REST API calls.

## Features
- Direct REST API communication without complex library abstractions.
- Secure environment variable credential handling.
- Validates properties before attempting an API call.
- Uses `rich` to provide an enhanced CLI UX with detailed table summarization.
- Writes comprehensive API request and standard error logs to `trading.log`.
- **Bonus Feature included**: Supports a third order type (`STOP_MARKET`) along with the classic `MARKET` and `LIMIT`. 

## Setup
1. **Clone/extract this repository.**
2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure API Keys:**
   - Create a `.env` file in the root directory (you can copy `.env.example`).
   - Add your Binance Futures Testnet keys:
     ```env
     BINANCE_API_KEY=your_testnet_api_key
     BINANCE_API_SECRET=your_testnet_api_secret
     ```

## Usage
Run the CLI using python from the root directory:

**Market Order:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**Limit Order:**
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 100000
```

**Stop Market Order:**
```bash
python cli.py --symbol BTCUSDT --side SELL --type STOP_MARKET --quantity 0.01 --price 90000
```

## Logs
Check `trading.log` for full details of request endpoints, JSON outputs, and REST error tracking. To evaluate this submission, provide your Testnet API keys in `.env` and execute the 2 bash commands above, then view the generated `trading.log`. You can zip this folder to deliver the final application payload.
