text = input("Enter text to save in file: ")

with open("notes.txt", "w") as file:
    file.write(text)

print("Text saved successfully.")

print("\nReading file content...\n")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)