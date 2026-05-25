number = int(input("Enter a number: "))

temp = number
power = len(str(number))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == number:
    print(f"{number} is an Armstrong Number")
else:
    print(f"{number} is NOT an Armstrong Number")
