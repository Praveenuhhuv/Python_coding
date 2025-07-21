quantity=int(input('enter the quantity: '))
cost=quantity*100
if cost > 1000:
    discount=cost*10/100
    total_cost=cost-discount
else:
    total_cost=cost
print('total cost: ',total_cost)