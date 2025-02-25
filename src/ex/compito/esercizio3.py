word = str(input("Type something: "))
reverse = ""

for char in word:
    reverse = char + reverse

print(reverse)