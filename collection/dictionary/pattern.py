pattern='ABCDFBCSDFGHI'#recursive charector
dict={}
for i in pattern:
    if i in dict:
        print("first recursive char", i)
        break
    else:
        dict[i]=1