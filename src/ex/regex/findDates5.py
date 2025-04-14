import re

def find_dates(text):
    dates : list[str] = re.findall(r"((?:0[1-9]|[12][0-9]|3[01])/(?:0[1-9]|1[0-2])/\d{4})", text)
    return print(dates)

text = "Le date importanti sono 09/04/2025 e 15/08/2023."

find_dates(text)
