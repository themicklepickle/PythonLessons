# testing the membership sing in and not in operators

user_string = input("Please enter a collection of letters: ")
letters = {}
for letter in user_string:
	if letter not in letters:
		letters[letter] = 1
	else:
		letters[letter] += 1

for k in sorted(letters):
	print("{0}: {1}".format(k, letters[k]))
