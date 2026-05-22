text = input("Enter Text: ")

wovel = 0
uppercase = 0

for char in text :
	if char.isupper() :
		uppercase+=1
		
for char in text :
	if char.lower() in ["a", "e", "i", "o", "u"] :
		wovel+=1
		
print(f"\nTotal Wovels in {text} = {wovel}")
print(f"Total Uppercases in {text} = {uppercase}")