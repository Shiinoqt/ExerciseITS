import re

def is_integer(s):
    return bool(re.match(r'^[+-]?\d+$', s))

print(is_integer("123"))  # True
print(is_integer("-123"))  # True
print(is_integer("+123"))  # True
print(is_integer("123.456"))  # False