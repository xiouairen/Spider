from datetime import date, time, datetime, timedelta
import Spider

def runTask(func, day=0, hour=0, min=0, second=0):
  # Init time
  now = datetime.now()
  strnow = now.strftime('%Y-%m-%d %H:%M:%S')
  print("now:",strnow)
  # First next run time
  period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
  next_time = now
  strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
  print("next run:",strnext_time)
  while True:
      # Get system current time
      iter_now = datetime.now()
      iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
      if iter_now >= next_time:
          # Get every start work time
          print("start work: %s" % iter_now_time)
          # Call task func
          func()
          print("task done.")
          # Get next iteration time
          next_time = iter_now + period
          strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
          print("next_iter: %s" % strnext_time)
          # Continue next iteration
          continue

# runTask(work, min=0.5)
runTask(Spider.downloadBooks, min=1)