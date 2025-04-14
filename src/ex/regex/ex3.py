import re

def mask_numbers(text):
    maskedtext: str = str(re.sub(r"\d+", "###", text))
    return maskedtext

text = "Il codice è 12345 e la data è 2025."

print(mask_numbers(text))