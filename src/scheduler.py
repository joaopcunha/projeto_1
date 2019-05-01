import logging
import schedule
import sys
import signal
import time

logging.info("ETL jobs initialized")
stop_thread = False

def first_job():
    pass
    #run do primeiro job

def second_job():
    pass
    #run do segundo job

def construct_schedule():
    schedule.every().day.at("00:00").do(first_job)
    schedule.every().monday.do(second_job)

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
