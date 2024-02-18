import threading
import time
import schedule

from trading import Trading


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


if __name__ == '__main__':
    trading = Trading()
    schedule.every(1).minute.do(run_threaded, trading.trade)

    while True:
        schedule.run_pending()
        time.sleep(1)
