import re

def is_valid_cap(cap):
    capCheck = bool(re.match(r"\d{5}", cap))
    return capCheck

print(is_valid_cap("70124"))
print(is_valid_cap("A0123")) 