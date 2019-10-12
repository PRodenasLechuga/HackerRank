def convertTupleToHash(tupleElement):
    return hash(tupleElement)

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    T = ()
    for x in integer_list:
        T = T + (x, )

    print(convertTupleToHash(T))