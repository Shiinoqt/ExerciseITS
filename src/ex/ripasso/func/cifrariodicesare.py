from string import ascii_lowercase

def caesar_cipher(text, key):
    letters = ascii_lowercase
    result = ''
    for char in text:
        if char.lower() in letters:
            index = letters.index(char.lower())
            shifted_index = (index + key) % 26
            new_char = letters[shifted_index]
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result

# Example usage:
if __name__ == "__main__":
    text = "Hello, World!"

    encrypted_text = caesar_cipher(text, 2)
    print(f"{encrypted_text}")
