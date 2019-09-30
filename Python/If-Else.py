#!/bin/python3

import math
import os
import random
import re
import sys

def checkIfOdd(number):
    return True if (number % 2) != 0 else False

def numberBetweenAandB(number, a, b):
    return True if (number <= a and number >= b) else False

if __name__ == '__main__':
    number = int(input().strip())

    print("Weird" if (checkIfOdd(number) or numberBetweenAandB(number, 20, 6)) else "Not Weird")