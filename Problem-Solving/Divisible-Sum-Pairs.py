#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    resultList = []
    i = 0
    while len(ar) > 1:
        listToAppend = [int(ar[0] + ar[i]) for i in list(range(1, len(ar)))]
        for element in listToAppend:    
            resultList.append(element)
        ar.pop(0)
    
    return len(list(filter(lambda x: x % k == 0, resultList)))

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(str(result))

