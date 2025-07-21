num1=int(input("Enter number: "))
temp=num1
cube=0
raiseto=len(str(temp))
while num1>0:
    num=num1%10
    cube+=num** raiseto
    num1=num1//10

if temp==cube:
    print("Armstrong")
else:
    print("Not an Armstrong Number")
