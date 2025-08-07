# I need to take a user's order, which has to be done one item per line.
# Then when the user has finished their order they must input control-d 
# which will end their input to the program.

def main():
    menu = 
{    
    Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

while true:
    try:
        item = input("Item:\n")
        print(item{cost})
    except KeyError:
        print("Sorry, that item is not on the menu, please try again.")
    except EOFError:
        print("\nItem: ")
        break
