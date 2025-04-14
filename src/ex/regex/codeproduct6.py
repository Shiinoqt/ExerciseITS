import re

def check_product_code(code):
    return print(bool(re.match(r"[A-Z]{4}-\d{4}-[A-Z]{2}", code)))

check_product_code("PROD-9876-ZX")
check_product_code("PROD-99-ZX")