lst=[1,9,11,3,4,6,7,8,7,5,3,2,5,7,10,15,16,12,10,8,7]
distrub=[]
for i in range(0,len(lst)-1):
    if (lst[i]>lst[i+1] and lst[i]>lst[i-1]) or (lst[i]<lst[i+1] and lst[i]<lst[i-1]):
        distrub.append(lst[i])
        #11>3               11>9                  2<5                2<3
    else:
        pass
print(distrub)