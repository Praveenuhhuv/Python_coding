f=open('wordcount','r')
dict={}
for i in f:
    data=i.rstrip('\n').split(' ')
    for i in data:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
del dict['']
for i,j in dict.items():
    print(i,":",j)
