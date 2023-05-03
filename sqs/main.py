# pip install
import sys
import os
import schedule
import time
import pytz

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import local modules: variables
from sqs.utils.process_messages import process_job_posting
from sqs.utils.process_messages import process_match_review


def main():
    central_tz = pytz.timezone("US/Central")
    schedule.every().day.at(time_str="03:00",tz=central_tz).do(process_job_posting)
    schedule.every().day.at(time_str="00:00",tz=central_tz).do(process_match_review)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()