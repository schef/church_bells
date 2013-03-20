#!/usr/bin/env python
# Python3
# Iscitavanje eventa iz crontab-a

from crontab import CronTab
from croniter import croniter
from datetime import datetime

def events_parser(number_of_events):
  cronuser = CronTab()
  list = []
  for job in cronuser:
    list.append(str(job).split(" "))
  
  events = []
  while list:
    cronstring = ""
    for i in range(5):
      cronstring += list[0][i]
      if i < 4:
        cronstring += " "
    command = list[0][5]
    comment = " ".join(map(str, list[0][7:]))
    iter = croniter(cronstring, datetime.now())
    for i in range(number_of_events):
      a = [command, iter.get_next(datetime), comment]
      events.append(a)
    list.pop(0)
  
  
  #events[0][1].strftime("%d/%m/%y %H:%M")
  events.sort(key=lambda tup: tup[1])
  return (events)
  #for i in events:
  #  print (i[1].strftime("%d/%m/%y %H:%M"), i[2], i[0])
