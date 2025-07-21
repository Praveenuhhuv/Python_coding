three=[]
five=[]
for i in range(1,20):
    if i % 3 == 0:
        three.append(i)
    elif i % 5 ==0:
        five.append(i)

print("divisible by 3: ",three)
print("divisible by 5: ",five)