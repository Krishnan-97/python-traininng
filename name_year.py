import datetime

name = input("Enter Name:")
age = int(input("Enter Age:"))

dt = datetime.datetime.today()
year = dt.year

gap = 100-age

print('Hi',name,'!!')
print('You will become 100 years old in the year',year+gap)

