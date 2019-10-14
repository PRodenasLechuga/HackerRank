#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    counter = 0
    barLen = len(s)
    result = 0
    for square in s:
        if (counter + m) <= barLen and sum([s[i] for i in range(counter, m + counter)]) == d:
            result += 1
            counter += 1
        else:
            counter += 1

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
