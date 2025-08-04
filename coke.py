#Creating the variable.

amount_due = 50

#Running a while loop until the amount due is greater than 0.
while amount_due > 0: 
    #Printing the amount still due, if necessary.
    print("Amount due :", amount_due)
    
    #Asking the user for their input, to insert a coin one at a time.
    coin = int(input("Please insert coins, one at a time: "))
    
    #checking if the coin is in the list. That list containing 25, 10, 5. 
    if coin in [25, 10, 5]:
        
        #Then subtracting that value from the amount_due.
        amount_due -= coin

#Calculating the change owed, getting the absolute value of amount_due.
change_owed = abs(amount_due)

#Printing the final result.
print("Change owed: ", change_owed)





