from bot.client import BinanceFuturesClient

def place_order(
    client: BinanceFuturesClient,
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
) -> dict:
    """
    Places an order on Binance Futures.
    """
    endpoint = "/fapi/v1/order"
    
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }
    
    if order_type == "LIMIT":
        params["timeInForce"] = "GTC"  # Good Till Cancel required for LIMIT
        params["price"] = price
    elif order_type == "STOP_MARKET":
        params["stopPrice"] = price   # Price at which the stop is triggered
        
    return client.post(endpoint, **params)
