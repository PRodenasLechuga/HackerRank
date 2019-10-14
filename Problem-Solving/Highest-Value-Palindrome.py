#!/bin/python3

import math
import os
import random
import re
import sys

# IT ONLY SOLVES 27/33 CASES
def highestValuePalindrome(s, n, k):  
    if n < k:
        return "9" * n
    
    reverseS = s[::-1]

    strLen = len(s)

    indexOfDifferences = [i for i in range(strLen) if s[i] != reverseS[i]]
    
    indexOfDifferencesLen = len(indexOfDifferences)

    indexArray = 0

    if indexOfDifferencesLen > 0:
        while indexOfDifferencesLen < k:
            if s[indexArray] != 9:
                s[indexArray] = 9
                k = k - 1
            
            if s[strLen - 1 - indexArray] != 9:
                s[strLen - 1 - indexArray] = 9
                k = k - 1
            indexArray = indexArray + 1
    else:
        if k % 2 != 0:
            s[int(strLen/2)] = 9
            k = k - 1

        i = 0
        changesMade = 0
        while changesMade < k:
            if s[i] != 9:
                s[i] = 9
                k = k - 1
                changesMade = changesMade + 1
                
            if s[strLen - 1 - i] != 9:
                s[strLen - 1 - i] = 9
                k = k - 1
                changesMade = changesMade + 1

            i = i + 1

                
    changesMade = 0

    while k != 0 and len(list(dict.fromkeys(s))) != 1 and changesMade < k:
        if indexOfDifferencesLen > 0:
            for i in indexOfDifferences:
                if s[i] != 9 and changesMade < k:
                    s[i] = 9
                    changesMade = changesMade + 1
                
                if s[strLen - 1 - i] != 9 and changesMade < k:
                    s[strLen - 1 - i] = 9
                    changesMade = changesMade + 1
        else:
            break
                
    s = ''.join(list(map(str, s)))
    reverseS = s[::-1]         
    indexOfDifferences = [i for i in range(strLen) if s[i] != reverseS[i]]
    
    return s if len(indexOfDifferences) == 0 else "-1"
    
    

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = list([int(x) for x in input()])

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()

