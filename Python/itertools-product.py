# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product



if __name__ == '__main__':
    firstList = map(int, input().split())
    secondList = map(int, input().split())

    print(' '.join(map(str, list(product(firstList,secondList)))))

