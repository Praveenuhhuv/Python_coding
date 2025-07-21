num1=int(input("Enter range: "))
for i in range(2,num1+1):
    if i>1:
        prime=True
        for j in range(2,i):
            if i % j ==0:
                prime=False
                break

        if not prime:
            print(i)
