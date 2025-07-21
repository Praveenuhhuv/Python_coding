dic={'id':101,'fname':'praveen','lname':'p','age':22,'prof':'bigdata','salary':1000000}
print(dic['age'])
# for i in dic:
#     print(i) print key values
for i in dic:
    print(i,":",dic[i])
dic['age']-=2
dic['new']='key'
print('fname' in dic)
print('mark'not in dic)
print(dic)