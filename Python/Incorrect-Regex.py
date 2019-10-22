# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def checkIfValid(regex):
    try:
        re.compile(regex)
        print('True')
    except re.error:
        print('False')


for _ in range(int(input())):
    checkIfValid(input())

