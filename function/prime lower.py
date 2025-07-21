upper=int(input("enter upper limit: "))
lower=int(input("enter lower limit: "))

for i in range(lower,upper+1):#2,10
    if i > 1:#2>1
        for j in range(2,i):#2t02
            if i%j==0:
                break
        else:
            print(i)