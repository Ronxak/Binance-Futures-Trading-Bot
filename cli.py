import os
import sys
import argparse
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.validators import validate_symbol, validate_side, validate_order_type, validate_quantity, validate_price
from bot.logging_config import logger

console = Console()

def load_credentials():
    load_dotenv()
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        console.print("[bold red]Error:[/bold red] API keys not found. Please set BINANCE_API_KEY and BINANCE_API_SECRET in your .env file.")
        sys.exit(1)
        
    return api_key, api_secret

def main():
    parser = argparse.ArgumentParser(description="Simplified Trading Bot for Binance Futures Testnet")
    parser.add_argument("--symbol", required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="Order side (BUY or SELL)")
    parser.add_argument("--type", required=True, dest="order_type", help="Order type (MARKET, LIMIT, STOP_MARKET)")
    parser.add_argument("--quantity", required=True, help="Quantity to trade")
    parser.add_argument("--price", "--stopPrice", dest="price", help="Required for LIMIT and STOP_MARKET orders")
    
    args = parser.parse_args()
    
    # 1. Validation
    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.order_type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)
    except ValueError as e:
        console.print(f"[bold red]Validation Error:[/bold red] {e}")
        logger.warning(f"Validation Error: {e}")
        sys.exit(1)

    # 2. Setup Client
    api_key, api_secret = load_credentials()
    client = BinanceFuturesClient(api_key, api_secret)

    console.print(Panel(f"Placing [bold cyan]{order_type}[/bold cyan] order for [bold yellow]{symbol}[/bold yellow]...", expand=False))
    
    # 3. Execution
    try:
        response = place_order(client, symbol, side, order_type, quantity, price if price > 0 else None)
        
        # 4. Display Output
        table = Table(title="Order Response Summary")
        table.add_column("Order ID", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Symbol")
        table.add_column("Side")
        table.add_column("Type")
        table.add_column("Executed Qty")
        table.add_column("Avg Price")

        table.add_row(
            str(response.get("orderId", "N/A")),
            str(response.get("status", "N/A")),
            str(response.get("symbol", symbol)),
            str(response.get("side", side)),
            str(response.get("origType", order_type)),
            str(response.get("executedQty", "0")),
            str(response.get("avgPrice", "0"))
        )
        
        console.print(table)
        console.print("\n[bold green]Success:[/bold green] Order placed successfully!")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] Failed to place order.")
        console.print(f"[red]{e}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()
