f=open('C:/Users/dell/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip("\n").split(',')
    # age=data[3]
    # if age<'30':
    #     print(data[1:])


    # loc=data[-1]
    # if loc=="india":
    #     print(data[1:5])

    # loc = data[-1]
    # age = data[3]
    # if loc == "india" and age > "50":
    #     print(data[1:4])

    # loc = data[-1]
    # if loc == "uk":
    #     print(data[1:5])

    loc = data[-1]
    prof = data[4]
    if loc == "india" and prof=='Doctor':
        print(data[1:4])
