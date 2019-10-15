#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.

def migratoryBirds(arr):
    typesOfBirdSeen = list(dict.fromkeys(arr))
    birdsTuples = []
    for typeOfBirdSeen in typesOfBirdSeen:
        birdsTuples.append((typeOfBirdSeen, sum(1 for x in arr if x == typeOfBirdSeen)))

    maxTimesTypeOfBirdSeen = max(list([t[1] for t in birdsTuples]))

    maxTypeBirdSeen = list([bird for bird in birdsTuples if bird[1] == maxTimesTypeOfBirdSeen])

    return min(list([typeOfBird[0] for typeOfBird in maxTypeBirdSeen]))


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result))

