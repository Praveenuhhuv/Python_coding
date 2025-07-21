# type of operation
# 1.union
# 2.intersection
# 3.difference
st1={1,3,5,6,8,0,9}
st2={2,4,6,8,3,9}
st3=st1.union(st2)
print(st3)
print("#"*100)
st4=st1.intersection(st2)
print(st4)
print("#"*100)
st5=st1.difference(st2)
print(st5)