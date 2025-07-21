upper=int(input("enter upper limit: "))
lower=int(input("enter the lower limit: "))
sum1=0
sum2=0
for i in range(lower,upper+1):
    if i % 2 == 0:
        sum1+=i
    else:
        sum2+=i
print(sum1,sum2)
        