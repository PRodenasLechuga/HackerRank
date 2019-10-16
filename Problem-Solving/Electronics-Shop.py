#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    possibleCombinations = []
    for x in keyboards:
        possibleCombinations.extend([(x + y) for y in drives])
    affordableCombinations = list(filter(lambda x: x <= b, possibleCombinations))
    return -1 if len(affordableCombinations) == 0 else max(affordableCombinations)



if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(str(moneySpent) + '\n')

