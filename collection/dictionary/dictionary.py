# how to define dictionary
# dict={}
#
# (key value pair)
dic={'id':101,'fname':'praveen','lname':'p','age':22,'prof':'bigdata','salary':1000000}
print(dic)#support hetrogenous data,inesetion order preserved
print("#"*100)
dic1={'id':101,'fname':'praveen','lname':'praveen','age':22,'age':'bigdata','salary':1000000}
dic1['age']=10000
#not support duplicate key,support duplicate value,mutable
print(dic1)