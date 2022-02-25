import re
import os
#import requests

d = {"Data":[]}
fmt = '(?P<month>.*) (?P<day>.*) (?P<time>.*) (?P<deviceName>.*) (?P<processName>.*)\[(?P<numberOfOccurrence>)\d\] \(.*\): (?P<description>.*)'
#fmt2 = '(?P<month>.*) (?P<day>.*) (?P<time>.*) (?P<deviceName>.*) (?P<processName>.*)\[(?P<numberOfOccurrence>\d+)\]: (?P<description>.*)'
path="./interview_data_set"
with open(path) as fd:
  for line in fd:
    obj = re.search(fmt,line)
    if obj == None:
      print("解析失败")
      continue
   #   print("-------")
   #   obj = re.search(fmt2,line)
   #   print(obj)
    print(obj.groupdict())
    d["Data"].append(obj)
#print(d)

#r=requests.post('https://foo.com/bar',data=d)
