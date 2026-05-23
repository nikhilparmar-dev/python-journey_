def is_prime(n) :
	if n <= 1 :
		return False
	
	elif n > 1 :
		for i in range(2, int(n**0.5) + 1) :
			if n % i == 0 :
				return False
				
		return True
		

no = int(input("Enter an number: "))
print("It is Prime" if is_prime(no) else "Not an Prime Number")