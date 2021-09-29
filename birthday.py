bday_dict = {
  "Krishnan": "3/6/1997",
  "Russel": "3/15/1994",
  "Duke": "1/17/1964",
  "Ramesh": "6/23/1964",
}
print("Welcome to the birthday dictionary. We know the birthdays of:")
for key, value in bday_dict.items():
  print(key)

inp = input("Whose b'day you wanna lookup:")

print(inp+"'s birthday is on",bday_dict[inp])