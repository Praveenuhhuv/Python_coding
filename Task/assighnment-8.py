age=int(input("enter the age: "))
if age>=18 and age<=120:
    print("you are eligible to vote")
elif age<18 and age>0:
    print("you are not eligible to vote")
else:
    print("age is valid between 0 to 120")