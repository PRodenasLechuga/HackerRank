# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    for _ in range(int(input())):
        n = input().split()

        try: 
            print(int(n[0])//int(n[1]))
        except Exception as error:
            print("Error Code: " + str(error))

