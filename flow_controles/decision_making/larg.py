number_1=int(input("enter 1st number: "))
number_2=int(input("enter 2st number: "))
number_3=int(input("enter 3st number: "))
if number_1 > number_2 & number_1 > number_3:
     print(number_1," is the largest")
elif number_3 > number_1 & number_3 > number_2:
    print(number_3, " is the largest")
else:
    print(number_2, " is the largest")