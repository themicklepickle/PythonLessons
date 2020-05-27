word = list("the waxwork man")
word[12:] = "woman wart"

word2 = ""
for letter in word:
	word2 += letter

print(word2)
