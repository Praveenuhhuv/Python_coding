missing=None
repeated=None
lst = [1, 2, 4,2, 6, 7, 9, 10]
n=len(lst)
for i in range(1, n + 1):
        if i not in lst:
            missing = i
        elif lst.count(i) > 1:
            repeated = i
sum1=missing +repeated
print(sum1)


