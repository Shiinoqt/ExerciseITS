while True:
    word = str(input("Type a word: "))
    if word[0] == word[-1]:
        print("The word has the same first and last character.")
    elif word.lower() == "quit":
        break
