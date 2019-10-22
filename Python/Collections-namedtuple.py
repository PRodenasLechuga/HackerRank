# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections


if __name__ == '__main__':
    n = int(input())
    columns = ','.join(input().split())
    Student = collections.namedtuple('Student', columns)

    add = 0
    for _ in range(n):
        S = Student(*(input().split()))
        add += int(S.MARKS)

    print(add/n)

