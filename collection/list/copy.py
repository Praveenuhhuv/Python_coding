lst=[1,2,3]
mutable=lst.copy()
var1=lst
var1.append(10)
mutable.append(2)
print(lst)
print(mutable,var1)