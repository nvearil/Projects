# 0,1,1,2,3,5,8,13,21,34,55

maximum_term = int(raw_input("Maximum term?:"))
current_term_value = 1
previous_term_value = 0

while (current_term_value + previous_term_value) < maximum_term:
	if (current_term_value + previous_term_value) == 1:
		previous_term_value = 1
		print(current_term_value)
		print(previous_term_value)
		
	elif (current_term_value + previous_term_value) == 2:
		current_term_value = 2
		print(current_term_value)
		
	else:
		term_holder = current_term_value
		current_term_value += previous_term_value
		previous_term_value = term_holder
		print(current_term_value)