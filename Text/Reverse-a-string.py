# Reverse a String
userInput = str(raw_input("Enter a string to be reversed:")) # take user input and convert to string
outputString = "" # blank placeholder variable for our reversed string

for i in range(len(userInput)): #loop to step through each character in string
    outputString = outputString + userInput[-i - 1]
    
# use our for loop counter and string indexing to step backwards through outputString
# we use "-i - 1"  here as first loop will produced outputString[0] which is not useful to us.
# after each step concat outputString and the return of our string index
    
print(outputString)