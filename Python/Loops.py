def returnSquared(number):
    integer = 0
    while integer < number:
        yield integer*integer
        integer+=1



if __name__ == '__main__':
    number = int(input())

    for number in returnSquared(number):
        print (number)