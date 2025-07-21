num=int(input())
rem=num%10
rem2=num//10
sum1=rem+rem2
if num % sum1==0:
    print(num, "number is harshad")
else:
    print(num,"number is not harshad")