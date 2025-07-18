#Greeting the user

greeting = input("Greetings user: ").lower().strip()

#Assigning strings to the numbers for each greeting

incorrect = (0.00)
partially_correct = (20.00)
correct = (100.00)

#Implementing a rule that if greeted with hello, the output will be $0

if greeting.startswith("hello"): 
    print ("You will now receive: $", format(incorrect, ",.2f"))

elif greeting.startswith("h"): 
    print ("You will now receive: $", format(partially_correct, ",.2f"))
    
else:
    print("You will now receive: $", format(correct, ",.2f"))
    
