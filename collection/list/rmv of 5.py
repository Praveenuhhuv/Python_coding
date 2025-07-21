lst=[15,3,20,25,18,52,30,55,16]
# for i in lst[:]:
#     if i % 5==0:
#         lst.remove(i)
# print(lst)
lst=[i for i in lst if i%5!=0]
print(lst)
# i=0
# while i<len(lst):
#     if lst[i]%5==0:
#         lst.pop(i)
#     else:
#         i+=1
# print(lst)