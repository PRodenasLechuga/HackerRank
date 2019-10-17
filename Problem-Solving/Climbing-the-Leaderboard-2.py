#!/bin/python3
#THIS CODE DIDN'T SOLVED ALL CASES DUE TO TIMEOUTS
import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):

    rankingScores = list(zip(scores, list(range(1, len(scores) + 1))))

    for score in alice:

        possibleRanking = list(filter(lambda x: x[0] <= score, rankingScores))

        if len(possibleRanking) == 0:
            yield len(scores) + 1
        else:
            result = possibleRanking[0]
            yield result[1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(dict.fromkeys(map(int, input().rstrip().split())))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

