def getIndexes(element, listToSearch):
    indexes = [i + 1 for i, e in enumerate(listToSearch) if e == element]
    return indexes
    


if __name__ == '__main__':
    n = list(map(int, input().split()))

    firstList = []
    secondList = []

    for i in list(range(0, n[0])):
        firstList.append(input())
    
    for i in list(range(0, n[1])):
        secondList.append(input())
        
    for x in secondList:
        print(-1 if x not in firstList else ' '.join(list(map(str,getIndexes(x, firstList)))))

