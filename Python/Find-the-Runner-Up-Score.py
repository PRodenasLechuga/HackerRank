def giveMeRunnerUp(arr,n):
    return sorted(set(arr), reverse=True)[1]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(giveMeRunnerUp(arr, n))