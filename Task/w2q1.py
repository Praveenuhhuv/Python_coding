def even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

num=int(input("enter the number: "))
result=even_odd(num)
print(num," is ",result)