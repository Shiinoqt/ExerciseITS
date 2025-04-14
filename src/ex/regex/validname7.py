import re

def is_valid_name(name):
    return print(bool(re.match(r'[A-Z][a-z]{2,}', name)))

is_valid_name("Marco") 
is_valid_name("marco")
is_valid_name("Ma")   