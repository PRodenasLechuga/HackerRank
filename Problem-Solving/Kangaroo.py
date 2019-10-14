#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def getCommonPointFromBothLists(list1, list2):
    return len([i for i in range(len(list1)) if list1[i] == list2[i]])
    

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (x1 < x2 and v1 < v2) or (x2 < x1 and v2 < v1) or (x1 != x2 and v1 == v2):
        return "NO"
    else:
        k = 5
        while True:
            path1 = [x1 + (v1 * i) for i in range(k)]
            path2 = [x2 + (v2 * i) for i in range(k)]
            if x1 < x2 and path1[-1] > path2[-1]:
                return "YES" if getCommonPointFromBothLists(path1, path2) > 0 else "NO"
            elif x2 < x1 and path2[-1] > path1[-1]:
                return "YES" if getCommonPointFromBothLists(path1, path2) > 0 else "NO"
            else:
                k = k + 5


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
