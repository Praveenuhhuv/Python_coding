#Looping-while,for
#1.initialization
#2.condition
#3.increment
# value = int(input("Enter the number of Fibonacci terms: "))  # Number of terms to generate
# valu1 = 0  # First term in the Fibonacci sequence
# value2 = 1  # Second term in the Fibonacci sequence
# count = 0  # Counter to track the number of terms printed
#
# while count < value:  # Continue until we print 'value' terms
#     print(valu1)  # Print the current term
#     nextvalue = valu1 + value2  # Calculate the next Fibonacci number
#     valu1, value2 = value2, nextvalue  # Update the two previous numbers
#     count += 1  # Increment the counter
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()
