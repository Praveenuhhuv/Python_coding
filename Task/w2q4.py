age = int(input("Enter your age: "))
sex=input('entr your sex(m/f): ').lower()
days=int(input('enter the number of days: '))

if 18<= age <30:
    wage_per_day=700 if sex=='m' else 750

elif 30<= age <=40:
    wage_per_day=800 if sex=='m' else 850
else:
    print("error in range")
    wage_per_day=0

total_wage=days * wage_per_day
if wage_per_day>0:
    print("total wage= ",total_wage)