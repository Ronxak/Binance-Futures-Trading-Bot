# 🤖 Binance Futures Testnet Trading Bot (Beginner Friendly)

Welcome to your automated trading bot! This is a simple, command-line application that connects directly to the **Binance Futures Testnet**. The "Testnet" is a safe, simulated environment where you can trade with fake money ("paper trading") to test your strategies without any real financial risk.

## 🧠 Trading Concepts for Beginners

If you are new to trading, here is what the different order types mean in plain English:

1. **MARKET Order**: "I want to buy/sell right now, whatever the current price is." This is the fastest way to enter or exit a trade.
2. **LIMIT Order**: "I want to buy/sell, but only if the price reaches a specific target." You set a price limit. The trade will sit and wait until the market hits your target.
3. **STOP_MARKET Order (Stop Loss)**: "I want to protect myself from losing too much money." You set a trigger price. If the market drops (or rises) to that price, the bot automatically fires a Market order to sell/buy and exit your position.

---

## 🚀 Key Features
- **Multi-Order Support**: Execute `MARKET`, `LIMIT`, and `STOP_MARKET` orders.
- **Enhanced Visuals**: Beautiful tables and real-time feedback in your terminal.
- **Secure**: All communication with Binance is encrypted and authenticated.
- **Error Protection**: Automatically checks if your quantities and prices make sense before sending them to Binance.

---

## 🛠 Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher installed on your computer.
- A [Binance Futures Testnet](https://testnet.binancefuture.com/) account.

### 2. Installation
Clone the repository and navigate into the project directory:
```bash
git clone https://github.com/Ronxak/Binance-Futures-Trading-Bot.git
cd trading_bot
```

### 3. Create a Virtual Environment (Recommended)
This keeps the project's tools separate from the rest of your computer:
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
Open `.env` and add your Testnet API keys (you can get these from your Binance Testnet dashboard):
```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

---

## 📈 How to Use the Bot (Commands)

Once everything is set up, you can run the bot from your terminal. Here are the most common commands you will use.

*(Make sure your virtual environment is active, meaning you see `(venv)` in your terminal).*

### 1. Market Order (Instant Buy)
**Scenario**: You think the price of Bitcoin is going up right now, and you want to buy immediately.
```bash
python3 cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### 2. Limit Order (Target Price)
**Scenario**: You currently own 0.01 BTC. You want to sell it for a profit, but only if the price hits exactly $100,000. The bot will place the order and wait patiently.
```bash
python3 cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 100000
```

### 3. Stop Market Order (Stop Loss)
**Scenario**: You own 0.01 BTC, but you are worried the market might crash. You tell the bot to automatically sell your Bitcoin if the price drops to $60,000, preventing further losses.
```bash
python3 cli.py --symbol BTCUSDT --side SELL --type STOP_MARKET --quantity 0.01 --stopPrice 60000
```

> **Note**: You can always flip the `--side` from `BUY` to `SELL` (or vice versa) depending on what you are trying to achieve!

---

## 📂 Project Structure
For the technically curious:
- `cli.py`: The main script you run. Handles the pretty terminal graphics.
- `bot/client.py`: The engine that securely talks to Binance.
- `bot/orders.py`: The logic that builds your orders (including smart routing for complex "Algo" orders).
- `bot/validators.py`: The safety checker that stops bad inputs.
- `trading.log`: A record file that tracks every move the bot makes.
