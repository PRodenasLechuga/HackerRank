def getSecondLowestGrade(studentList):
    scores = list(dict.fromkeys([student[0] for student in studentList]))
    secondLowestGrade = sorted(scores)[1]
    return sorted(filter(lambda x: x[0] == secondLowestGrade, studentList), key = lambda x: x[1])

if _name_ == '_main_':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((score,name))

    for student in getSecondLowestGrade(students):
        print(student[1])