import schedule
import time
#import shopclues


def start1():
    exec(open("wbot.py").read())
    

schedule.every(1).minutes.do(start1)


# Checks whether a scheduled task
# is pending to run or not
while True:
    schedule.run_pending()
    time.sleep(1)