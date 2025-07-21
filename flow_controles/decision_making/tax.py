price=int(input("enter price of the bike: "))
if price > 100000:
    tax=0.15 * price
elif 50000<=price<=100000:
   tax= 0.10 * price
else:
    tax= 0.05 * price
print("road tax of the bike: ",tax)