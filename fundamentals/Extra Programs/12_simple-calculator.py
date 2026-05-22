no1 = int(input("Enter First Number: "))
opr = input("Select an Operator(+,-,*,/): ")

if opr not in ("+", "-", "*", "/") :
        print("Invalid Operator Selected, try again")
else :         
    no2 = int(input("Enter Second Number: "))

    if opr == "+" :
        print(f"Result : {no1 + no2}")
    elif opr == "-" :
        print(f"Result : {no1 - no2}")
    elif opr == "*" :
        print(f"Result : {no1 * no2}")
    elif opr == "/" :
    	print(f"Result : {no1 / no2}")