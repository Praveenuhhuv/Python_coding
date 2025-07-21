f = open('C:/Users/dell/Downloads/temper.unknown', 'r')
dict = {}
for i in f:
    data = i.rstrip("\n").split(',')
    loc=data[0]
    value=data[1]
    if loc not in dict:
        dict[loc] = value
    else:
        old=dict[loc]
        if old<value:
            dict[loc]=value
        else:
            pass

for i, j in dict.items():
    print(i, ":", j)
