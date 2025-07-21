lst=[1,2,32,3,8,7,9]
def binary(serch):
    lower=0
    upper=len(lst) -1
    lst.sort()
    while lower<=upper:
        midd=(upper+lower)//2
        if serch>lst[midd]:
            lower=midd+1
        elif serch<lst[midd]:
            upper=midd-1
        elif serch==lst[midd]:
            return midd#flag=1,break
    return -1
serch=int(input("enter elm to searh: "))
result=binary(serch)
if result==-1:
    print("elment is not found")
else:
    print("element is found")