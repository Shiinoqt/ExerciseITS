import re

def find_codes(text):
    codes : list[str] = re.findall(r'[\d|\w]{8}', text)
    return print(codes)

text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
find_codes(text)
