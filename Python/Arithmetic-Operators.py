def applyFunction(a, b, func):
    return func(a ,b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(applyFunction(a, b, (lambda a,b: a + b)))
    print(applyFunction(a, b, (lambda a,b: a - b)))
    print(applyFunction(a, b, (lambda a,b: a * b)))