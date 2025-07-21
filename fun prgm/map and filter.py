# lst=[1,2,3,4,5,6,7,8,9,10]-squrq and add to new list
#
# lst1=[] map needed situation
# for i in lst:
#     lst1.apppend(i**2)
# print(lst1)
lst=[1,2,3,4,5,6,7,8,9,10]
lst1=list(map(lambda num:num**2,lst))
print(lst1)


# last=[1,2,3,4,5,6,7,8,9] filter needed situation
# lst1=[]
# for i in last:
#     if i%2==0:
#         lst1.append(i)
# print(lst1)
lst=[1,2,3,4,5,6,7,8,9,10]
lst1=list(filter(lambda num:num%2==0,lst))
print(lst1)
