#!/bin/python3

import math
import os
import random
import re
import sys

def getSign(x):
    return 1-(x<0)

def getSignChange(a,b):
  return 1 if (getSign(a) == 1 and getSign(b) == 0) else 0

# Complete the countingValleys function below.
def countingValleys(n, s):
    stepArray = list([1 if step == "U" else -1 for step in s])
    path = []
    path.append(0)
    sumInt = 0
    for i in list(range(0, len(stepArray))):
        sumInt += stepArray[i]
        path.append(sumInt)
    return sum(getSignChange(path[i], path[i + 1]) for i in list(range(0, len(path) - 1)))

if __name__ == '__main__':
    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(str(result) + '\n')

