import re

def validip(address: str) -> bool:
    pattern = r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
    if re.match(pattern, address):
        return True
    return False

print(validip("192.168.0.1"))
print(validip("256.256.256.256"))
print(validip("192.168.0.a"))


def validip2(address: str) -> bool:

    address = address.split('.')

    for part in address:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
        
    return True


print(validip2("192.168.0.1"))
print(validip2("256.256.256.256"))
print(validip2("192.168.0.a"))