f=open('C:/Users/dell/Downloads/sample4.txt','r')
for i in f:
    data=i.rstrip("\n").split(',')
    #print(data)
    age=data[3]
    if age=="21":
        print(data[1:5])