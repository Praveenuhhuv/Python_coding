# add empty list 1 to 100
# lst=[]
# for i in range(1,101):
#     lst.append(i)
# print(lst)
#
# list compreshension-3 methords
# methord1-range of eladd to the list(1-25)
lst=[i for i in range(1,26)]
print(lst)
lst1=[i for i in range(1,16)]
print(lst1)
lst=[(i,i**3) for i in range(1,16)]
print(lst)
print("#"*100)
# methord2-range of eladd to the list based on 1 condition

lst=[i for i in range(1,31) if i%2==0]
print(lst)
lst=[i for i in range(1,31) if i%5==0]
print(lst)
lst=[(i,i**2) for i in range(1,26) if i%2==0]
print(lst)
print("#"*100)
# methord3-more than 1 condition
lst1=[(i,i**2) if i%2==0 else i**3 for i in range(1,31)]
print(lst1)
lst1=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,31)]
print(lst1)
