def is_leap(year):
    return True if ((year % 100) == 0 and (year % 400) == 0) else True if ((year % 4) == 0 and not (year % 100) == 0) else False

year = int(input())
print(is_leap(year))