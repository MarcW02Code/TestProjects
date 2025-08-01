#Prompting the user for their input

camelcase = input("Please enter the name of your variable, keep in mind it must be in camel case: ")

#Printing the final output, starting with the label "snake_case", and making sure to continue the argument on the same
#line instead of starting a new one each time.

print("snake_case: ", end="")

#Adding a flag to remember if the previous character in the for loop was uppercase

was_prev_upper = False
is_first_char = True

#Setting up a for loop to go through each character in the input string.

for c in camelcase:
#if the character is in lowercase, print the character directly.
    if c.islower():
        print(c, end="")
        was_prev_upper = False #Resetting the flag
        is_first_char = False

    elif c.isupper():
        if not was_prev_upper and not is_first_char:
            print("_" + c.lower(), end="")
#If the character is uppercase, convert it to lowercase.
        else:
            print(c.lower(), end="") 
        was_prev_upper = True
        is_first_char = False

print("")