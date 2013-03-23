#!/usr/bin/env python
# Python3
#Usage: prog <priority number> <action>

import sys
sys.path.append("/home/zvona/church_bells/bin")
from events_parser import events_parser
from datetime import datetime
import collections
import os

def print_to_file(priority, play, message):
  with open('/home/zvona/church_bells/log/check_double_dates.log', 'a') as the_file:
    the_file.write(str(datetime.now()) + " " + priority + " " + play + " " + message + '\n')

list = events_parser(1)
list_of_dates = []
for i in list:
  list_of_dates.append(i[1])
if [x for x, y in collections.Counter(list_of_dates).items() if y > 1]:
  #provjeri prioritet
  if int(sys.argv[1]) > 1:
    #sviraj
    print_to_file(sys.argv[1], sys.argv[2], "sviram")
  else:
    print_to_file(sys.argv[1], sys.argv[2], "cekam")
else:
  #sviraj
  print_to_file(sys.argv[1], sys.argv[2], "sviram, sam sam")
