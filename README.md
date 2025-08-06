# TestProjects
Testing to see if github is easier for me to use for these test projects than gitlab.

# Problem set 2, question 1:
The way I want to approach this is by setting up a command that prompts the user for a variable name, called camelcase, and will end up outputting the variable's name in snake case instead of in camel case.
After that line I want to print out the snake case version of the camel case word, but I am making use of the 'end=""' argument to make sure that each changed letter goes to the end of the line instead of starting a new line. So that when the print command runs again it continues on the same line.
As I want to loop through the input and check to see if all characters are lower case, and if not how I can convert them, I googled examples of conversions to lower case in python and how to concisely write it. The rest of the code is fairly straight forward, I have included comments to show my mental workings throughout the problem.

# Problem set 2, question 2:
So for the coke program i want to be able to do a few things off the top of my head:
Firstly, the machine sells bottles of coke for 50cents each, so only when the total number of inputs equate to 50 will the correct result be outputted.
    > To do this I want to create an argument that somehow checks "if the amount input is == 50" change owed must output 0.
        > I must specify if the user must still input more coins. They can only put one in at a time.
    > (Some ideas)
        # if (" ") == 50:
        print(correct_amount)
Secondly, the machine only accepts coins in denominations of 25 cents, 10 cents, and 5 cents, anything not multiplicable by these numbers is incorrect.
*I can assume the user will only be inputting integers, any denomination that is not accepted will be ignored.

I wrote some rough code and tried to mindmap it out, but was unsure of whether to use an if or while loop, and how to go about checking the number in the best way possible. I watched "Dors Coding School" explain this exact problem and how they did it, hence the similarities in what I have done compared to them. I looked up some other peoples methods of how they got the answer, but they were very different to the method that I wanted to implement. 

# Problem set 2, question 3:

For the twttr problem, I want to set up a program that promopts the user for a string of text, and then returns the same text but with vowels omitted.
Off the top of my head this is my thinking:
    > I want to create a list with the vowel letters in it.
    > I want to take the user's input and check it for any of those vowels in the list
    > Then return the new input with vowels omitted.





