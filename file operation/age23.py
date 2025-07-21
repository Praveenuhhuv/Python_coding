f=open('C:/Users/dell/Downloads/sample4.txt','r')
for i in f:
    data=i.rstrip("\n").split(',')
    #print(data)
    loc=data[5]
    age = data[3]
    if loc=="Chennai" and age>"23":
        print(data[1:5])