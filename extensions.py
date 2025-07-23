#Prompting the user for a file name

filename = input("Please enter your file name: ").lower().strip()

#Setting up a rule in which the user's input will be tested against.

#if the file name ends in the following strings then the system will print the text "image/" followed by the user's input, splitting the user's input at
#the period . With "-1" grabbing the last part of the file, the extension.
if filename.endswith(('.gif', '.png', '.jpeg', '.jpg')):
    if filename == "jpg":
        filename = "jpeg"
    print(f'image/{filename.split(".")[-1]}')
#The same step is repeated below, except I am adding "application" instead of "image" as the following extensions are not images, rather applications.
elif filename.endswith(('.pdf', '.zip')):
    print(f'application/{filename.split(".")[-1]}')
#The same step is repeated below, except I am adding "text" instead of anything else as the following extensions are not images, rather plain text files.
elif filename.endswith('.txt'):
    print("text/plain")
#Finally I am setting a rule so that any other user input will output the following application.
else:
    print("application/octet-stream")
