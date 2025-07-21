first_side=int(input("enter the length of first_side: "))
second_side=int(input("enter the length of second_side: "))
third_side=int(input("enter the length of third_side: "))

if first_side==second_side==third_side:
    print('An equilateral triangle ')
elif first_side==second_side or first_side==third_side or second_side==third_side:
    print('isosceles triangle')

else:
    print('scalene triangle')