# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()

list1 = set(list(map(int, input().split())))

n = input()

list2 = set(list(map(int, input().split())))

for x in sorted(list1.difference(list2).union(list2.difference(list1))):
    print(x)

