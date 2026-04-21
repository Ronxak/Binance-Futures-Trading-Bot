def validate_symbol(symbol: str) -> str:
    """Validate symbol format loosely (alphanumeric)."""
    symbol = symbol.upper()
    if not symbol.isalnum():
        raise ValueError(f"Invalid symbol format: {symbol}. Must be alphanumeric.")
    return symbol

def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ("BUY", "SELL"):
        raise ValueError(f"Invalid side: {side}. Must be BUY or SELL.")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    # Bonus: supporting STOP_MARKET
    valid_types = ("MARKET", "LIMIT", "STOP_MARKET")
    if order_type not in valid_types:
        raise ValueError(f"Invalid order type: {order_type}. Must be one of {', '.join(valid_types)}.")
    return order_type

def validate_quantity(quantity: str) -> float:
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError()
        return qty
    except ValueError:
         raise ValueError(f"Invalid quantity: {quantity}. Must be a strictly positive number.")

def validate_price(price: str, order_type: str) -> float:
    if order_type.upper() in ("LIMIT", "STOP_MARKET"):
        if not price:
            raise ValueError(f"Price must be provided for {order_type} orders.")
        try:
            p = float(price)
            if p <= 0:
                raise ValueError()
            return p
        except ValueError:
            raise ValueError(f"Invalid price: {price}. Must be a strictly positive number.")
    return 0.0
