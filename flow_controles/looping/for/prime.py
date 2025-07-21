# num=int(input("enter the number: "))
# flag=0;
# for i in range(2,num):
#     if num % i ==0:
#         flag=1
#         break
# if flag ==1:
#     print("number is not prime")
# else:
#     print("number is prime")
# Get input from user
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

print(f"Prime numbers between {lower} and {upper} are:")

# Loop through the range
for num in range(lower, upper + 1):
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to sqrt(num)
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
