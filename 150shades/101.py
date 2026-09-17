sentence = input("Enter a sentence: ")
words = sentence.split()
capitalized = []
for word in words:
    capitalized.append(word[0].upper() +
    word[1:])
print(" ".join(capitalized))
