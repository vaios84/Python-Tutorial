
import schedule
import time
from datetime import datetime


def job():
    print("I'm working...")
    # Returns a datetime object containing the local date and time
    dateTimeObj = datetime.now()
    print(dateTimeObj)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    schedule.every(1).minutes.do(job)
    # schedule.every().hour.do(job)
    # schedule.every().day.at("10:30").do(job)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(job)
    # schedule.every().minute.at(":17").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
