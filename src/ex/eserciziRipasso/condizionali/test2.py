def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        stipendio = ore_lavorate*10

    else:
        ore_supplemento = ore_lavorate - 40
        stipendio = 40*10 + ore_supplemento*15

    return stipendio
    
print(calcola_stipendio(40))
print(calcola_stipendio(30))
print(calcola_stipendio(45))
print(calcola_stipendio(60))
print(calcola_stipendio(0))