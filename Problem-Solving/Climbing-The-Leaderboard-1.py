#!/bin/python3
#THIS CODE DIDN'T SOLVED ALL CASES DUE TO TIMEOUTS
import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    newScores = []
    for aliceScore in alice:
        newScores = scores.copy()
        newScores.append(aliceScore) 
        newScores.sort(reverse = True)
 
        yield newScores.index(aliceScore) + 1     


if __name__ == '__main__':
    scores_count = int(input())

    scores = list(dict.fromkeys(map(int, input().rstrip().split())))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print('\n'.join(map(str, result)))
    print('\n')

    

