lower= int(input("enter the lower limit: "))
upper=int(input("enter the upper limit: "))#upper limit
sum1=0
sum2=0
while (lower <= upper):
    if lower % 2 == 0:
        sum1+=lower
    else:
        sum2+=lower
    lower+=1
print("even no. sum=",sum1,",odd no. sum=",sum2)