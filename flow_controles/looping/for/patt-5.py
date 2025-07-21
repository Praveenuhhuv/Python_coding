for i in range(1,6):#i=1,2,3
    for j in range(5,i-1,-1):#j=1,2,3 j=1,2,3 j=1,2,3
        print(i,end=' ')#i=1,1,1 2,2,2 3,3,3
    print()

for i in range(1,6):#i=1,2,3
    for j in range(i,6):#j=1,2,3 j=1,2,3 j=1,2,3
        print(i,end=' ')#i=1,1,1 2,2,2 3,3,3
    print()