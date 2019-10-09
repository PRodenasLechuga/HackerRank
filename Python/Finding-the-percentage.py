def getScoresAverage(studentName, studentsList):
    return sum(studentsList[studentName])/(len(studentsList[studentName]))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print("%.2f" % getScoresAverage(query_name, student_marks))