import re

def find_cf(text):
    cf : list[str] = re.findall(r'[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]', text)
    return print(cf)

testo = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."
find_cf(testo) # ['RSSMRA85M01H501Z', 'BNCMRA85T41H501Y']