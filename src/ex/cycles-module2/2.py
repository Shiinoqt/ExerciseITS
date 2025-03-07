# ex. 2
ns = int(input("Cars from North-south: "))
eo = int(input("Cars from East-ovest: "))
soglia = int(input("Soglia auto: "))
time = int(input("Time priority: "))

if ns > soglia:
    if eo > soglia:
        timeNs = 50
        timeEo = 50
    else:
        timeNs = time
        timeEo = 100 - time
elif eo > soglia:
    timeNs = 100 - time
    timeEo = time
else:
    tot = ns + eo
    timeNs = ns/tot*100
    timeEo = 100 - timeNs
print(f"Time given to NS: {timeNs}, Time given to EO: {timeEo}")