import datetime
x, y = map(int, input().split())
print(["MON","TUE","WED","THU","FRI","SAT","SUN"][datetime.date(2007,x,y).weekday()])