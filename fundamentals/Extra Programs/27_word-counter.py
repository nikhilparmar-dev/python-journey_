sentence = input("Enter a sentence: ")

word_count = len(sentence.split())
character_count = len(sentence)
space_count = sentence.count(" ")

print("\n===== RESULT =====")
print("Total Words:", word_count)
print("Total Characters:", character_count)
print("Total Spaces:", space_count)