lst=[1,2,3,4,5,6,7,8,9,10]
lst1=list(filter(lambda num:num%2!=0,lst))
lst2=list(map(lambda num:num**3,lst1))
print(lst2)