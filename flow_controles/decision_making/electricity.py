unit=int(input("enter the amout unit used: "))
if unit>200:

     unit_1 = unit - 200
     amount = 5 * 100 + 10 * unit_1
elif 100< unit <=200:
     amount = 5 * unit - 100
else:
     amount="Free"
print("Bill amount is ",amount)