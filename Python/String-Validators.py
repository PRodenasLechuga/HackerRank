def isAlphaNumeric(s):
    return any(char.isalnum() for char in s)

def hasAlpha(s):
    return any(char.isalpha() for char in s)

def hasNumeric(s):
    return any(char.isdigit() for char in s)

def isLower(s):
    return any(char.islower() for char in s)

def isUpper(s):
    return any(char.isupper() for char in s)

if __name__ == '__main__':
    s = input()

    print(isAlphaNumeric(s))
    print(hasAlpha(s))
    print(hasNumeric(s))
    print(isLower(s))
    print(isUpper(s))



