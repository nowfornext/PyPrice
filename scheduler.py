from config import *

from pytz import timezone

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.executors.pool import ThreadPoolExecutor

from os import remove as rm

def createScheduler():

    jobstores = {
        'default': SQLAlchemyJobStore(url='sqlite:///%s'%(schedueler_jobStore_SQLite_file))
    }

    executors = {
        'default': ThreadPoolExecutor(8)
    }

    job_defaults = {
        'coalesce': False,
        'max_instances': 3
    }

    scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=timezone('Europe/Paris'))
    
    return scheduler

def resetScheduler():

    try:
        rm(schedueler_jobStore_SQLite_file)
        return 0
    except FileNotFoundError:
        return 1
    except :
        return -1