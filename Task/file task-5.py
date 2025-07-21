f=open('C:/Users/dell/Downloads/movies_cleaned_pandas.csv','r')
count=0
for i in f:
    data = i.strip("\n").split(',')
    rate=float(data[3])
    year=int(data[2])
    movie=data[1]
    if 1915>=year<=1986:
        count+=1
print(count)