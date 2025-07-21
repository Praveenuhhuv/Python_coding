line='cat rat bus cat rat bus rat rat bus cat car car bus rat'
dict={}
data=line.split(' ')
for i in data:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)