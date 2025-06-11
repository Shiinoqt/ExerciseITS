from string import ascii_lowercase

# def caesar_cipher(text, key):
#     result = []
#     for char in text:
#         if char.isalpha():
#             shift = key % 26
#             base = ord('a') if char.islower() else ord('A')
#             new_char = chr((ord(char) - base + shift) % 26 + base)
#             result.append(new_char)
#         else:
#             result.append(char)
#     return ''.join(result)


# Example usage:
# if __name__ == "__main__":
#     original_text = "Hello, World!"
#     key = 3
    
#     encrypted_text = caesar_cipher(original_text, key)
#     print(f"Encrypted: {encrypted_text}")
    