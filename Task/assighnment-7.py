def comparison(num1,num2):
    less=num1<num2
    great=num1>num2
    equl=num1==num2
    noteql=num1!=num2
    geql=num1>=num2
    leql=num1<=num2
    return less,great,equl,noteql,geql,leql

num1=int(input("enter the number1: "))
num2=int(input("enter the number2: "))

less,great,equal,noteql,geql,leql=comparison(num1,num2)
print(f"num1<num2: {less}")
print(f"num1>num2: {great}")
print(f"num1==num2: {equal}")
print(f"num1!=num2: {noteql}")
print(f"num1>=num2: {geql}")
print(f"num1<=num2: {leql}")