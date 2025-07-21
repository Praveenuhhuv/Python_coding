# 1.how we define?
# 2.hetrogenous support
# 3.duplicates allowed
# 4.insertion  order preserved or not??(same oder the number insert it give output)
# 5.mutable or not
# ********************
# list=[]#variable name=[] emty list
# print(type(list))
# lst=list()#methord used-variable name=list()emty list
string='sxda'
lst1=list(string)
print(lst1)
#list is da of python which is orderd,allow duplicate,hetro and mutable
lst=[1,2,32,3,8,7,9]
def binary(serch):
    lower=0
    upper=len(lst)-1
    midd=(upper+lower)//2
    lis=sorted(lst)
    while lower<=upper:
        if serch>lis[midd]:
            lower=midd+1
        elif serch<lis[midd]:
            upper=midd-1
        elif serch == lis[midd]:
            return midd
    return -1
serch=int(input("enter elm to searh: "))
result=binary(serch)
if result==-1:
    print("elment is not found")
else:
    print("element is found")