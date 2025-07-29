def xor_cipher(text: str, key: int) -> list[int]:
    numbers = []

    for char in text:
        xor_value = ord(char) ^ key
        numbers.append(xor_value)

    return numbers


def xor_decipher(numbers: list[int], key: int) -> str:
    decrypted_text = ""

    for number in numbers:
        decrypted_char = chr(number ^ key)
        decrypted_text += decrypted_char

    return decrypted_text


if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    key = int(input("Enter key: "))

    encrypted_numbers = xor_cipher(text, key)
    print(f"\nEncrypted numbers:", encrypted_numbers)

    key2 = int(input(f"\nEnter key for decryption: "))
    decrypted_text = xor_decipher(encrypted_numbers, key2)
    print(f"\nDecrypted text:", decrypted_text)