#Acronym Extractor

print("Automatic Acronym Maker")
text = input("Type a sentence: ").strip().title()

first_letters = [word[0] for word in text.split()]
print("".join(first_letters))

