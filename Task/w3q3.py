num1=int(input("Enter number: "))
res=0
while num1>0:
    rem=num1%10
    res=res*10+rem
    num1=num1//10
print(res)
