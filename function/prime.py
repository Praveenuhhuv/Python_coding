def prime(num):
    flag=0
    for i in range(2,num):
        if num % i == 0:
            flag=1
            break
    if flag!= 0:
        return "number is prime"
    else:
        return "number is not prime"

data=prime(9)
data1=prime(11)
print(data)
print(data1)