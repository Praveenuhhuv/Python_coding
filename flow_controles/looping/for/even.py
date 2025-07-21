upper=int(input("enter upper limit: "))
lower=int(input("enter the lower limit: "))
for i in range(lower,upper+1):
    if i % 2 == 0:
        print(i,end=",")