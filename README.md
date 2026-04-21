# 🤖 Binance Futures Testnet Trading Bot

A robust, modular Python CLI application built to execute trades on the **Binance Futures Testnet (USDT-M)**. Designed with clean architecture, strict input validation, and comprehensive logging for professional-grade reliability.

## 🚀 Key Features
- **Multi-Order Support**: Execute `MARKET`, `LIMIT`, and `STOP_MARKET` orders.
- **Enhanced CLI UX**: Real-time feedback and structured order summaries using the `rich` library.
- **Secure Authentication**: HMAC-SHA256 signature generation for direct REST API communication.
- **Structured Logging**: Every request, response, and error is tracked in `trading.log`.
- **Validation Layer**: Pre-flight checks on symbols, quantities, and prices to prevent unnecessary API errors.

---

## 🛠 Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher.
- A [Binance Futures Testnet](https://testnet.binancefuture.com/) account.

### 2. Installation
Clone the repository and navigate into the project directory:
```bash
git clone https://github.com/Ronxak/Binance-Futures-Trading-Bot.git
cd trading_bot
```

### 3. Create a Virtual Environment (Recommended)
Isolate your dependencies to keep your system clean:
```bash
# MacOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Credentials
Create a `.env` file in the root directory by copying the template:
```bash
cp .env.example .env
```
Open `.env` and add your Testnet API keys:
```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

---

## 📈 Usage Examples

### Placing a Market Order
Buys 0.01 BTC at the current market price.
```bash
python3 cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Placing a Limit Order
Sells 0.01 BTC when the price reaches 100,000 USDT.
```bash
python3 cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 100000
```

### Example CLI Output
When an order is successfully placed, you will see a detailed summary:
```text
╭────────────────────────────────────╮
│ Placing LIMIT order for BTCUSDT... │
╰────────────────────────────────────╯
                          Order Response Summary                          
┏━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┳━━━━━━┳━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Order ID    ┃ Status ┃ Symbol  ┃ Side ┃ Type  ┃ ExecQty    ┃ Avg Price ┃
┡━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━╇━━━━━━╇━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ 13058485527 │ NEW    │ BTCUSDT │ SELL │ LIMIT │ 0.0000     │ 0.00      │
└─────────────┴────────┴─────────┴──────┴───────┴────────────┴───────────┘
[SUCCESS] Order placed successfully!
```

---

## 📝 Assumptions & Constraints
1.  **Binance Futures Testnet**: All requests are routed to `https://testnet.binancefuture.com`. This bot is not intended for the production environment without modifications.
2.  **Lot Size Requirements**: The `quantity` provided must respect the minimum lot size and precision requirements of the specific trading pair (e.g., 0.001 BTC for BTCUSDT).
3.  **Authentication**: Users must provide valid Testnet credentials. Invalid keys will return a `-2015` error.
4.  **Network**: A stable internet connection is required for real-time REST API requests.

---

## 📂 Project Structure
- `cli.py`: Main entry point and CLI UI logic.
- `bot/client.py`: API layer handling signatures and request dispatching.
- `bot/orders.py`: High-level order placement logic.
- `bot/validators.py`: Input validation for CLI arguments.
- `trading.log`: Generated at runtime, containing full API audit trails.
