from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from subprocess import call
import os

os.environ['TZ'] = 'UTC'

sched = BlockingScheduler()

def hourly_job():
    call(["python", "src/arbitrage-hour.py"])

def daily_job():
    call(["python", "src/arbitrage-hour.py"])

sched.add_job(hourly_job, CronTrigger.from_crontab('5 * * * *'))
sched.add_job(daily_job, CronTrigger.from_crontab('1 0 * * *'))

sched.start()