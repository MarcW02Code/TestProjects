#Prompting the user for their input

camelcase = input("Please enter the name of your variable, keep in mind it must be in camel case: ")

#Printing the final output, starting with the label "snake_case", and making sure to continue the argument on the same
#line instead of starting a new one each time.

print("snake_case: ", end="")

#Setting up a for loop to go through each character in the input string.

for c in camelcase:
#if the character is in lowercase, print the character directly.
    if c.islower():
        print(c, end="")

#If the character is uppercase, convert it to lowercase but make sure to add an underscore before it, then print it.
    else:
        print("_" + c.lower(), end="") 

print("")