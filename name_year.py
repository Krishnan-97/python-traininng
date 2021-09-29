import datetime

name = input("Enter Name:")
age = int(input("Enter Age:"))

def getYear(age):
    dt = datetime.datetime.today()
    year = dt.year

    gap = 100 - age

    return year+gap

ans = getYear(age)

print('Hi',name,'!!')
print('You will become 100 years old in the year',ans)

