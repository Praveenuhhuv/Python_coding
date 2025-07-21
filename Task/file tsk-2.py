f=open('C:/Users/dell/Downloads/movies_cleaned_pandas.csv','r')
count=0
for i in f:
    data = i.strip("\n").split(',')
    rate=float(data[3])
    year=int(data[2])
    movie=data[1]
    if rate>4 and year>2005:
        count+=1
print(count)