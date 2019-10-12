

def insertIntoList(index,value):
    intList.insert(index,value)

def removeElement(elementToRemove):
    intList.remove(elementToRemove)

def appendElementToList(elementToAppend):
    intList.append(elementToAppend)

def sortList():
    return sorted(intList, key=int)

def popLastElement():
    intList.pop()

def reverseList():
    return intList[::-1]

if __name__ == '__main__':
    N = int(input())
    intList = []
    for _ in range(0, N):
        commandList = input().split()

        if commandList[0] == "insert":
            insertIntoList( int(commandList[1]), commandList[2] )
        elif commandList[0] == "print":
            print("[" + ", ".join(str(x) for x in intList) + "]")
        elif commandList[0] == "remove":
            removeElement(commandList[1])
        elif commandList[0] == "append":
            appendElementToList(commandList[1])
        elif commandList[0] == "sort":
            intList = sortList()
        elif commandList[0] == "pop":
            popLastElement()
        elif commandList[0] == "reverse":
            intList = reverseList()
