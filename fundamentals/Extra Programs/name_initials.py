full_name = input("Enter full name: ")

parts = full_name.split()

for part in parts:
    print(part[0].upper(), end=" ")
