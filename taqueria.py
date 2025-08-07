# I need to take a user's order, which has to be done one item per line.
# Then when the user has finished their order they must input control-d 
# which will end their input to the program.

while true:
    try:
        item = input("Item:\n")
        print(item{cost})
    except KeyError:
        print("Sorry, that item is not on the menu, please try again.")
    except EOFError:
        print("\nItem: ")
        break
