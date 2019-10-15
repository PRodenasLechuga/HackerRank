#!/bin/python3

import math
import os
import random
import re
import sys


def getTotalX(a, b):
    result = []
    for i in list(range(max(a), min(b) + 1)):
        if sum(1 for x in a if i % x == 0) == len(a) and sum(1 for x in b if x % i == 0) == len(b):
            result.append(i)

    return len(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

