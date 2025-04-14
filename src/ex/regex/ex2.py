import re

def extract_emails(text):
    emails:list[str] = re.findall(r"\w+@\w+\.[a-z]{2,3}\.*[a-z]*", text)
    return emails

text:str = "Contattaci a info@azienda.com oppure support@help.org"

print(extract_emails(text))