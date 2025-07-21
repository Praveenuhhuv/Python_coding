num1=int(input("Enter number: "))
sum=0
for i in range(1,num1):
    if num1%i==0:
        sum+=i
if sum==num1:
    print('prefect number')
else:
    print('not perfect number ')