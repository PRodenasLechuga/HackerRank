#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesDistance = [ int(a) + int(x) for x in apples ]
    orangesDistance = [ int(b) + int(x) for x in oranges ]
    houseFloor = range(int(s), int(t) + 1)

    return sum([1 for x in applesDistance if x in houseFloor]), sum([1 for x in orangesDistance if x in houseFloor]) 
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    for result in countApplesAndOranges(s, t, a, b, apples, oranges):
        print(result)

