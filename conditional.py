import datetime

dt = datetime.datetime.today()
day = dt.day

if(day % 2 == 0):
    print("Today's date is even.")
else:
    print("Today's date is odd")