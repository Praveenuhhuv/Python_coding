data='luminar technolab'
count=0
vowels=[i for i in data if i in 'aeiouAEIOU']
print(len(vowels))

non_vowel=[i for i in data if i not in 'aeiouAEIOU']
print(len(non_vowel))