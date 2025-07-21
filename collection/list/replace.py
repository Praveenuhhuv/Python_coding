lst=["hi","hello","old","name","old"]
# lst=str(lst)
# lst=lst.replace("old","new")
print(lst)
for i in range(len(lst)):
    if lst[i] =="old":
        lst[i]="new"
print(lst)