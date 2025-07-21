user=int(input())
lst=[12,50,9,20,56,13,15,25]
flag=0
for i in lst:
    if user in lst:
        flag=1
        break
    else:
        pass
if flag==1:
    print("found")
else:
    print("not found")