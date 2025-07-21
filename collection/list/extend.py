lst=[2,5,7,10,12]
lst1=[11,6,7,8]
lst.extend([2,3,4,5])
lst.extend(lst1)
x=str(lst)
x=x.replace("[","")
x=x.replace("]","")
print(x)