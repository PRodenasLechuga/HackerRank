#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    return sum(x > 0 for x in arr)/len(arr), sum(x < 0 for x in arr)/len(arr), sum(x == 0 for x in arr)/len(arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for result in plusMinus(arr):
        print("%.6f" % result)
