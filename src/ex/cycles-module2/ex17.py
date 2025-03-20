tMax: int = -float("inf")
dMax: int = 0

tMin: int = float("inf")
dMin: int = 0

normal: int = 0

tMedia: int = 0

i = 1

while i < 7:
    
    temp = float(input("Insert temperature: "))
    
    tMedia += temp

    if temp > tMax:
        tMax = temp
        dMax = i
    
    if temp < tMin:
        tMin = temp
        dMin = i
    
    if temp >= 10 and temp <= 30:
        normal += 1
        if normal == 7:
            print("Temperature nella norma")

    elif temp < 5 or temp > 35:
        print("Allerta temperatura")

    i += 1

tMedia = tMedia/7
tMedia = round(tMedia, 1)

print(f"La temperatura media è di: {tMedia}\nLa temperatura massima è di: {tMax} nel giorno {dMax}\nLa temperatura minima è di: {tMin} nel giorno {dMin}")
