f=open('C:/Users/dell/Downloads/customer1.txt','r')
dict={}
for i in f:
    data=i.rstrip("\n").split(',')
    pro=data[4]
    if pro in dict:
        dict[pro] += 1
    else:
        dict[pro] = 1


for i, j in dict.items():
    print(i, ":", j)

