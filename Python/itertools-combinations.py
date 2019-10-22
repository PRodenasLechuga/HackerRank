# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

problemInput = input().split()

for i in range(int(problemInput[1]) + 1):
    for x in list(combinations(sorted(list(problemInput[0])), i)):
        if x:
            print(''.join(x))


