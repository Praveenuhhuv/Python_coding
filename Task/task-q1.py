height=float(input("enter your height(in meters): "))
sq_height=height**2
weight=int(input("enter your weight(in kilograms): "))
BMI=weight/sq_height
if BMI < 18.5 :
    print("Underweight")
elif BMI < 24.9 :
    print("Normal Weight")
elif BMI < 29.9:
    print("Overweight")
else:
    print("Obesity")