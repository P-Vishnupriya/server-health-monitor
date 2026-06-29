import logging
 
logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
 
logger = logging.getLogger()