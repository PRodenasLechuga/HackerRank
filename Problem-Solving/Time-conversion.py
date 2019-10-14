#!/bin/python3

import os
import sys
import datetime
#
# Complete the timeConversion function below.
#
AMPM = ""
hour = ""
def timeConversion(s):
    AMPM = ''.join(x for x in s if x.isalpha())
    hour = ''.join(x for x in s if not x.isalpha())
    date_time = datetime.datetime.strptime(hour, '%H:%M:%S')   

    return date_time + datetime.timedelta(hours=12) if AMPM == "PM" and date_time.hour != 12 else date_time
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = "Date :" + timeConversion(s).strftime('%H:%M:%S')

    if ''.join(x for x in s if x.isalpha()) == "AM":
        result = result.replace("Date :12:", "00:")

    f.write(result.replace("Date :", "") + '\n')

    f.close()
