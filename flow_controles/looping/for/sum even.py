upper=int(input("enter upper limit: "))
lower=int(input("enter the lower limit: "))
sum=0
for i in range(lower,upper+1):
    if i % 2 == 0:
        sum+=i
print(sum)