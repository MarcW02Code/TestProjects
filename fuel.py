#Take in an input

while True:

#Make sure the input is formatted as x/y, wherein x and y are both positive integers, and
#outputs as a percentage how much fuel is in the tank, rounded to the nearest integer.

    try:
        fuel = input("Fraction: ")   
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)
        
        if x < 0 or y < 0 or x > y:
            continue 

        x = x * 100
        p = x / y
        p = round(p)

        if 100 >= p >= 99:
            print(f"F")
            break

        elif p > 100:
            pass

        elif p <= 1:
            print(f"E")
            break

        else:
            print(f"{p}%")
            break

    except(ValueError, ZeroDivisionError):
        pass
    
     
    



