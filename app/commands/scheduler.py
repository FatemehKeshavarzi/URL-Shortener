import time
import schedule
from app.tasks.url_tasks import delete_expired_urls 

def run_scheduler():
    schedule.every(60).seconds.do(delete_expired_urls)
    print("Scheduler started... Press Ctrl+C to stop.")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped manually.")


if __name__ == "__main__":
    run_scheduler()