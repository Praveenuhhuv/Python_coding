main_str=input("Enter the main string: ").split()
sub_str=input("Enter the sub string: ")
if sub_str in main_str:
    print("Substring found")
else:
    print("Substring not found")