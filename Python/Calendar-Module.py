import datetime
import calendar

def findDay(date): 
    born = datetime.datetime.strptime(date, '%m %d %Y').weekday() 
    return (calendar.day_name[born])

if __name__ == '__main__':
    print(findDay(input()).upper()) 

