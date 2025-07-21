lst1=[(i,"small") if i<16 else (i,"medium") if 16<=i<36 else (i,"large")  for i in range(1,50)]
print(lst1)