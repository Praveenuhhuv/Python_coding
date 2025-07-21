no_class_held=int(input("enter no. class held: "))
attend=int(input("number of class attended: "))
percentage=(attend/no_class_held)*100
print("percentage: ",percentage)
if percentage < 75:
    print("not alloed to sit in exam")
else:
    print("alloed to sit in exam")