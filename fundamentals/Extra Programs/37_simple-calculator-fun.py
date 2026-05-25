def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("===== CALCULATOR =====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice: ")

if choice == "1":
    print("Result:", add(num1, num2))

elif choice == "2":
    print("Result:", subtract(num1, num2))

elif choice == "3":
    print("Result:", multiply(num1, num2))

elif choice == "4":
    print("Result:", divide(num1, num2))

else:
    print("Invalid choice.")
