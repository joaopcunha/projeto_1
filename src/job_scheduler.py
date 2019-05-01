import logging
import schedule
import sys
import signal
import time

from jobs import city_info_job
from jobs import daily_etl_job

logging.info("ETL jobs initialized")
stop_thread = False

def construct_schedule():
    schedule.every().day.at("00:00").do(daily_etl_job.run_job)
    schedule.every().monday.do(city_info_job.run_job)

def start():
    construct_schedule()

    while not stop_thread:
        schedule.run_pending()
        time.sleep(1)

def stop():
    stop_thread = True

def signal_handler(signal, frame):
    logging.warning('stopping job')
    stop()
    sys.exit(1)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    start()
