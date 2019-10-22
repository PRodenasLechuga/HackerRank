from itertools import permutations


if __name__ == '__main__':
    problemInput = list(map(str,input().split()))
    
    for x in sorted(permutations(list(map(str,problemInput[0])), int(problemInput[1]))):
        print(''.join(x))

