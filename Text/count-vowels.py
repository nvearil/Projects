vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0

user_input = raw_input("> ")

for i in range(len(user_input)):
	a = user_input[i - 1]
	if a in vowels:
		vowel_count += 1

print "%i vowels in string \"%s\"" % (vowel_count, user_input)