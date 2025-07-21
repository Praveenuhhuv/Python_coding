f=open('fruits','r')
f1=open('not_apple','w')
for i in f:
    if i.strip() =='apple':#i not in 'apple\n':
           pass
    else:
        f1.write(i)