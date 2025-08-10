import logging
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Generate a timestamped log file
log_filename = datetime.now().strftime("logs/log_%Y-%m-%d_%H-%M-%S.log")

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()  # This prints to console too
    ]
)

# You can create a logger object to import elsewhere
logger = logging.getLogger("content-assistant")
def log_interaction(input_text, response_text):
    logger.info(f"User Input: {input_text}")
    logger.info(f"AI Response: {response_text}")

