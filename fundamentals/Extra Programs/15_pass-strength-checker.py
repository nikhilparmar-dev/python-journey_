password = input("Enter Your Password: ")

# Track our three conditions
has_length = len(password) >= 8
has_digit = False
has_upper = False

# Check for digits and uppercase letters in a single loop
for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True

# Count how many conditions are True
score = 0
if has_length:
    score += 1
if has_digit:
    score += 1
if has_upper:
    score += 1

# Output the final result based on the score
if score == 3:
    print("Strong Password")
elif score == 2:
    print("Medium Password")
else:
    print("Weak Password")
