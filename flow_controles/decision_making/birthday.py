current_year=int(input("enter the current year: "))
current_month=int(input("enter the current month: "))
current_day=int(input("enter the current day: "))
birth_year=int(input("enter  your birth year: "))
birth_month=int(input("enter  your birth month: "))
birth_day=int(input("enter  your birth day: "))

age=current_year - birth_year
if current_month >=birth_month:
    if current_month == birth_month:
        if current_day>=birth_day:
            print("your are ",age," old")
        else:
            age-=1
            print("your are ", age, " old")
    else:
        print("your are ", age, " old")
else:
    age -= 1
    print("your are ", age, " old")
