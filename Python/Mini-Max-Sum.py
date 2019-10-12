#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    totalSum = sum(arr)
    print(str(totalSum - max(arr)) + " " + str(totalSum - min(arr))) 

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
