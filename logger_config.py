import logging
import os

# Ensure the logs directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    filename='logs/routing.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Get the logger instance
logger = logging.getLogger(__name__)

# Optional: Add console handler for debugging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
