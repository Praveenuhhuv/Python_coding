def calculator(num1,num2,operator):
    if operator=='+':
        print("your answer is:",num1+num2)
    elif operator=='-':
        print("your answer is:", num1 - num2)
    elif operator=='*':
        print("your answer is:", num1 * num2)
    elif operator=='/':
        print("your answer is:", num1 / num2)
    elif operator == '%':
        print("your answer is:", num1 % num2)
    else:
        print("wrong input")

num1=int(input("Enter First number: "))
num2=int(input("Enter Second number: "))
operator=input("Enter Operator:")
calculator(num1, num2, operator)