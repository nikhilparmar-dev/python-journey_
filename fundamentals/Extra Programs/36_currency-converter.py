USD_TO_INR = 83

while True:
    print("\n===== Currency Converter =====")
    print("1. INR to USD")
    print("2. USD to INR")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inr = float(input("Enter INR amount: ₹"))
        usd = inr / USD_TO_INR
        print(f"${usd:.2f}")

    elif choice == "2":
        usd = float(input("Enter USD amount: $"))
        inr = usd * USD_TO_INR
        print(f"₹{inr:.2f}")

    elif choice == "3":
        print("Exiting converter...")
        break

    else:
        print("Invalid choice.")
