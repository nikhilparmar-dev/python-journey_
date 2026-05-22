try:
    # Take input and convert to floating-point number
    marks = float(input("Enter student marks: "))

    # Handle invalid marks first
    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter a value between 0 and 100.")
    
    # Evaluate grades based on rules
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")

except ValueError:
    # Handle non-numeric inputs like alphabets or symbols
    print("Invalid input! Please enter a valid number.")
