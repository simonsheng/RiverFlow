import time
import schedule
import logging
from datetime import datetime

# Configure the log handler
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scheduler.log'),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

logger = logging.getLogger(__name__)

def job():
    """Function to be executed by the scheduled task."""
    logger.info("Task started")
    # Place the code you want to execute here
    logger.info("Task completed")

def run_scheduler():
    """Start the scheduler."""
    logger.info("Scheduler started")

    # Configure scheduled tasks
    schedule.every(10).seconds.do(job)  # Run every 10 seconds
    # schedule.every().day.at("10:00").do(job)  # Run daily at 10:00 AM
    # schedule.every().monday.do(job)  # Run every Monday
    # schedule.every().minute.at(":30").do(job)  # Run every minute at the 30th second

    try:
        while True:
            schedule.run_pending()  # Run all pending tasks
            time.sleep(1)  # Prevent high CPU usage
    except KeyboardInterrupt:
        logger.info("Scheduler stopped")

if __name__ == "__main__":
    run_scheduler()