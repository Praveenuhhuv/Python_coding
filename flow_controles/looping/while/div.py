lower= int(input("enter the lower limit: "))
upper=int(input("enter the upper limit: "))#upper limit
while (lower <= upper):
    if lower % 5 == 0:
        print(lower,end=" ")
        lower += 1
    else:
        lower +=1