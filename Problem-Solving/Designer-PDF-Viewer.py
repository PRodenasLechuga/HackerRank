#!/bin/python3

import math
import os
import random
import re
import sys

def getAlphabet():
    return list("abcdefghijklmnopqrstuvwxyz")
# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alphabetHeight = zip(getAlphabet(), h)
        
    lettersInWord = list(dict.fromkeys(list(word)))

    heightArray = []
    
    for alphabetTuple in alphabetHeight:
        heightArray.append([int(alphabetTuple[1]) for letter in lettersInWord if alphabetTuple[0] == letter])
        
    return sum(max(list(heightArray)) * len(word))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
