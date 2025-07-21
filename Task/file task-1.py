f=open('C:/Users/dell/Downloads/movies_cleaned_pandas.csv','r')
# row=len(f.readlines())
row=0
for i in f:
    row+=1
print(row)
