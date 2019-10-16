#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    differentElements = list(dict.fromkeys(a))

    if len(differentElements) == 1:
        return len(a)
        
    frequencyOfELements = list([a.count(x) for x in list(range(min(differentElements), max(differentElements) + 1))])

    countOfPairs = []

    for i in list(range(0, len(frequencyOfELements) - 1)):
        countOfPairs.append(frequencyOfELements[i] + frequencyOfELements[i + 1])

    return max(countOfPairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()


