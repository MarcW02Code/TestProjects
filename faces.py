def convert_emoji(user_input):
    converted_input = user_input.replace(":)", "🙂")
    converted_input = converted_input.replace(":(", "🙁" )
    return converted_input
text_input = input("Please enter a sentence: ")
converted_sentence = convert_emoji(text_input)
print(converted_sentence)

