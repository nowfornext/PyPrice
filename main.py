from apscheduler.triggers.cron import CronTrigger

from scheduler import createScheduler, resetScheduler
from priceChecker import resetPriceChecker
from jobLoader import loadJobsToScheduler


def main():

    resetScheduler() ; resetPriceChecker()
    scheduler = createScheduler()
    loadJobsToScheduler(scheduler)

    scheduler.start()


if __name__ == "__main__":
    main()