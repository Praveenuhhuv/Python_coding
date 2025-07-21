# lst=[i for i in range(1,1001) if i%7==0]
# print(lst)

lst1=[num  for num in range(1,1001) if '3' in str(num)]
print(lst1)

string='Practice list compehension problems to drill your head'
lst2=[i for i in string if ' ' in i]
print(len(lst2))

vowels=[i for i in string if i in 'aeiouAEIOU']
print(len(vowels))

non_vowel=[i for i in string if i not in 'aeiouAEIOU' and i!=' ']
print(len(non_vowel))
data=string.split(' ')
len=[i for i in data if len(i)<5]
print(len)