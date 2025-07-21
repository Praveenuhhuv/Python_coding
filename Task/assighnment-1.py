import keyword

checker = input("Enter the string: ")

if checker.isidentifier() and not keyword.iskeyword(checker):
    print("The given string is a valid identifier.")
else:
    print("The string is not a valid identifier.")
