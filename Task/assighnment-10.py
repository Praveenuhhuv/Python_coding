num=int(input("enter the number: "))
def fact(num):
    if num==0:
        return 1
    else:
        return num * fact(num-1)
value=fact(num)
print(f"The factorial of {num} is: {value}")