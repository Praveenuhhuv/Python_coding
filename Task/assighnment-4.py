import keyword
def generate_strings(chars, n):
    all_strings = []

    def backtrack(current):
        if len(current) == n:
            all_strings.append(current)
            return

        for char in chars:
            backtrack(current + char)

    backtrack("")
    return all_strings
chars = input("Enter the string to create combinations from: ")
n = int(input("Enter the length of the strings: "))
result = generate_strings(chars, n)
print(f"All possible strings of length {n}:")
for string in result:
    if string.isidentifier() and not keyword.iskeyword(string):
        print(string)
    else:
        pass