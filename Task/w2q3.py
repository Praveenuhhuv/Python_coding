def great(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1,"is the greatest")
    elif num2>num1 and num2>num3:
        print(num2, 'is the greatest')
    elif num3>num1 and num3>num2:
        print(num3 ,"is the greatest")
    else:
        print("error in input")

num1=int(input("enter the number: "))
num2=int(input("enter the number: "))
num3=int(input("enter the number: "))
great(num1, num2, num3)