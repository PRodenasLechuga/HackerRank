#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max = scores[0]
    min = scores[0]
    numMax = 0
    numMin = 0

    for i in range(1, len(scores)):
        if scores[i] > max:
            max = scores[i]
            numMax += 1
        if scores[i] < min:
            min = scores[i]
            numMin += 1

    return numMax, numMin
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
