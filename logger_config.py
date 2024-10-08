from loguru import logger

# Remove any existing handlers
logger.remove()

logger.add("logs", rotation="1 week")

def get_logger():
    # Configure the logger
    return logger