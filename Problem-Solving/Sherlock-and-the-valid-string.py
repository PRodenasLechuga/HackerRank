#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    letters = list(dict.fromkeys([char for char in s]))

    ocurrencesArray = [s.count(letter) for letter in letters]
    
    frequencyOfOcurrences = list(dict.fromkeys(ocurrencesArray))

    return 'YES' if (len(frequencyOfOcurrences) == 2 and ocurrencesArray.count(1) == 1) or (len(frequencyOfOcurrences) < 3 and (max(ocurrencesArray) - min(ocurrencesArray) <= 1) and ((ocurrencesArray.count(max(ocurrencesArray)) < 2) or (len(frequencyOfOcurrences) == 1))) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
