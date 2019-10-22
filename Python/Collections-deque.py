# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

def append(element):
    d.append(element)

def appendleft(element):
    d.appendleft(element)

def pop():
    d.pop()

def popleft():
    d.popleft()


if __name__ == '__main__':
    d = deque()
    for _ in range(int(input())):
        problemInput = input().split()

        if problemInput[0] == "append":
            append(problemInput[1])
        elif problemInput[0] == "appendleft":
            appendleft(problemInput[1])
        elif problemInput[0] == "pop":
            pop()
        elif problemInput[0] == "popleft":
            popleft()

    print(" ".join(d))

