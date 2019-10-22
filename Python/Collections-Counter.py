from collections import Counter


if __name__ == '__main__':
    n = input()

    availableShoes = Counter(list(map(str, input().split())))

    n = int(input())

    earnedMoney = 0

    for i in list(range(1, n + 1)):
        clientOrder = input().split()

        if availableShoes[clientOrder[0]] > 0:
            earnedMoney += int(clientOrder[1])
            availableShoes[clientOrder[0]] -= 1

    print(earnedMoney)


