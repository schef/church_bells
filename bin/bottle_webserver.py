#!/usr/bin/env python
# Python3

from bottle import route, run
import sys
sys.path.append('./')
from events_parser import events_parser

@route('/events/<number>')
def events(number):
  list = events_parser(int(number))
  html = ""
  for i in list:
    string = ("<pre>" + i[1].strftime("%d/%m/%y %H:%M") + " <b>" + i[2] + "</b> (<i>" + i[0] + "</i>)</pre>\n")
    html += string
  return (html)


run(host='0.0.0.0', port=8080, debug=True)
