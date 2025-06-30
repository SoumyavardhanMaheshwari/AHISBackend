from django.core.management.base import BaseCommand
from datetime import datetime
import pytz
from ...models import Schedule
from ...models import Status
from time import sleep

class Command(BaseCommand):
    help = 'Run infinite background script'
    def handle(self,*args,**options):
        self.stdout.write('Starting schedule checking script...')

        while True:
            try:
                IST = pytz.timezone('Asia/Kolkata')

                datetime_ist = datetime.now(IST)

                hour = datetime_ist.hour
                minute = datetime_ist.minute
                all_objs = Schedule.objects.all()
                stats = Status.objects.all()
                #turning ON according to schedule
                for e in all_objs:
                    if e.hour <= hour and hour <= e.hour + e.duration//60:
                        if minute <= e.minutes:
                            stats[0].status = True
                    else:
                        if stats[0].status == True and stats[1].status == True:
                            continue
                        else:
                            stats[0].status = False
            except(KeyError):
                print("some error occurred:" +KeyError)
            sleep(60)

