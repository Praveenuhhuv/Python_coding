from random import choice

print("1.addition\n2.sub\n3.multiplication\n4.division")

def calculater(num1,num2,choice):
    if choice==1:
        result=num1+num2
    elif choice ==2:
        result=num1-num2
    elif choice ==3:
        result=num1*num2
    elif choice ==4:
        result=num1/num2
    else:
        result="wrong choice"
    return result

num1=int(input("enter number1: "))
num2 = int(input("enter number2: "))
choice=int(input("enter choice-1,2,3,4: "))
output=calculater(num1,num2,choice)
print(output)
