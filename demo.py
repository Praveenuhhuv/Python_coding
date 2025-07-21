print("hello")

num=int(input())
one=str(num)
if one==one[::-1]:
    print("palindrome")
else:
    print("Given number is not palindrome")