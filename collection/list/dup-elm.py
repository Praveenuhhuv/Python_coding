lst=[10,15,10,15,20,20,30,30,15,10,50,10]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)
