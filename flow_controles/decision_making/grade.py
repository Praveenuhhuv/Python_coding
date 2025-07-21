subject_1=int(input("Enter sunject 1's mark: "))
subject_2=int(input("Enter sunject 2's mark: "))
subject_3=int(input("Enter sunject 3's mark: "))
subject_4=int(input("Enter sunject 4's mark: "))
total=subject_1+subject_2+subject_3+subject_4
print("Total mark: ",total)
if (total >= 180):
    print("A+ grade")
elif (160 <= total <= 179):
    print("A grade")
elif (140 <= total <= 159):
    print("B+ grade")
elif (120 <= total<=139):
    print("B grade")
elif (100 <= total <= 119):
    print("C+ grade")
elif (80 <= total <= 99):
    print("C grade")
else:
    print("below 80 fail")
