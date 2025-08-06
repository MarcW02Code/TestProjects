#Prompt the user for input

a = input("Please input your sentence here: ")

vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']

result = ""

for char in a:
    if char not in vowels:
        result += char

print(result)