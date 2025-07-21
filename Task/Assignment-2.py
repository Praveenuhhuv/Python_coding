import keyword

dict=[]
checker=input("enter the string: ")
data=checker.split(' ')
for i in data:
    if i.isidentifier() and not keyword.iskeyword(i):
        dict.append(i)
    else:
        pass
print(f"the valid identifiers {dict}")