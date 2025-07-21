lis=[]
lis=[i for i in range(1,101)]
print(sum(lis))
even=[i for i in lis if i%2==0]
odd=[i for i in lis if 1%2!=0]
print("even sum=",sum(even))
print("odd sum= ",sum(odd))