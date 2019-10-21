def mutate_string(string, position, character):
    strList = list(string)
    strList[position] = character
    return ''.join(strList)


