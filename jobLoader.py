import traceback
from os import listdir
import yaml

from priceChecker import checkPrice


def loadJobsToScheduler(scheduler):
    
    jobs_to_load = listdir('./jobs')
    for job_to_load in jobs_to_load:
        try :
            with open('./jobs/%s'%(job_to_load), 'r') as f:
                
                job_data = yaml.load(f)
                scheduler.add_job(
                    checkPrice,
                    kwargs={
                        'url' : job_data["url"],
                        'priceSelector' : job_data["priceSelector"],
                        'alias': job_data["alias"],
                        'pbToken': job_data['pbToken'] if 'pbToken' in list(job_data.keys()) else None
                    },
                    trigger = 'cron',
                    year = job_data['cron']['year'] if 'year' in list(job_data['cron'].keys()) else '*',
                    month = job_data['cron']['month'] if 'month' in list(job_data['cron'].keys()) else '*',
                    week = job_data['cron']['month'] if 'week' in list(job_data['cron'].keys()) else '*',
                    day_of_week = job_data['cron']['day_of_weeks'] if 'day_of_weeks' in list(job_data['cron'].keys()) else '*',
                    hour = job_data['cron']['hour'] if 'hour' in list(job_data['cron'].keys()) else '*',
                    minute = job_data['cron']['minute'] if 'minute' in list(job_data['cron'].keys()) else '*',
                    second = job_data['cron']['second'] if 'second' in list(job_data['cron'].keys()) else '*'
                )
        except Exception as e:
            traceback.print_exc()
