def caclculator(num1,num2):
    sum=num1+num2
    mul=num1*num2
    div=num1/num2
    mod=num1%num2
    return sum,mul,div,mod

num1=int(input("enter the number1: "))
num2=int(input("enter the number2: "))

sum,mul,div,mod=caclculator(num1,num2)
print(f"Sum: {sum}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
print(f"Modulus: {mod}")
