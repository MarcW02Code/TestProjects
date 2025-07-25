#Prompting the user for an expression

expression = input("Please enter your expression: ")

#splitting the string into a sequence of values

x, y, z = expression.split(" ")

#converting the values of x and z into float numbers

x = float(x)
z = float(z)

#calculating results depending on the input of the user.

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "/":
    result = x / z
elif y == "*":
    result = x * z

#rounding the result to 1 decimal place

print(f"{result: .1f}")

