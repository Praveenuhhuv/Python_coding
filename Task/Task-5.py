score=int(input("Enter the score: "))
if score >= 90:
    print("Grade A")
elif 80 <= score <90:
    print("Grade B")
elif 70 <= score <80:
    print("Grade C")
elif 60 <= score <70:
    print("Grade D")
else:
    print("Fail")