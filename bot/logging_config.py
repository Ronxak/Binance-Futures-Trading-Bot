import logging

def setup_logger():
    # Create logger
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)
    
    # Create file handler which logs to trading.log
    fh = logging.FileHandler('trading.log')
    fh.setLevel(logging.INFO)
    
    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    # Add handler to the logger
    logger.addHandler(fh)
    
    return logger

logger = setup_logger()
