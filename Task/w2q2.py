def leap(year):
    if year % 4== 0 and year % 100 != 0 or year % 400 == 0:
        return "is a leap year"
    else:
        return "is not a leap year"

year=int(input("enter the year: "))
result=leap(year)
print(year, ' ',result)