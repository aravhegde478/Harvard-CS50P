import emoji

string = input("Enter a string: ")
emoji_result = emoji.emojize(string, language='alias')
print(emoji_result)