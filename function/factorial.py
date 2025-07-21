# def fact():
#     mul=1
#     num=int(input("enter the number: "))
#     for i in range(1,num+1):
#         mul*=i
#     print(mul)
#
# fact()
# fact()


# def fact(num):
#     mul = 1
#     for i in range(1, num + 1):
#         mul *= i
#     print(mul)
#
# fact(10)
# fact(8)
def fact(num):
    mul = 1
    for i in range(1, num + 1):
        mul *= i
    return mul



data1=fact(10)
data2=fact(6)
print(data1,data2)


