number=int(input("Enter the number to check: "))
if number % 2 == 0 and number % 3 == 0:
    print(number, " is divisible by 2 and 3")
else:
    print(number, " is not divisible by 2 and 3")