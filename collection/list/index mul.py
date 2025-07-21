from operator import index

lst=[1,6,7,10,4,8,12]
mul=[]
for index,value in enumerate(lst):  # Use enumerate to get both index and value
    mul.append(value**(index+1))
print(mul)
# pow=1
# for i in lst:
#     mul.append(i**pow)
#     pow+=1
# print(mul)
# for i in range(len(lst)):
#     mul.append(lst[i]**i)
#     pow+=1
# print(mul)