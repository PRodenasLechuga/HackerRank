#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    pages = list(range(0, n + 1))
    if n % 2 == 0:
        pages.append(0) 

    return min([int(pages.index(p) / 2), int(pages[::-1].index(p) / 2)])

if __name__ == '__main__':
    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(str(result) + '\n')

