from loguru import logger

logger.add("logs", rotation="1 week")

def get_logger():
    # Configure the logger
    return logger