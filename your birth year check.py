import datetime
b=int(input("Enter your birth year:"))
p=datetime.date.today().year
age=p-b
print("Your age=",age)
