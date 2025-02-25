from collections import Counter

pari = 0
dispari = 0
totale = 0
i = 1
media = 0

nums = []

while True:
    num = int(input("Inserisci Numero: "))
    nums.append(num)
    if num % 2 == 0:
        pari += num
    elif num % 2 != 0:
        totale += num
        media = totale / i
        i += 1
    if num == 0:
        break

counter = Counter(nums)
common = counter.most_common(1)[0][0]

print(f"Somma dei numeri pari: {pari}")
print(f"Media dei numeri dispari: {round(media, 2)}")
print(f"Numeri più frequenti: {common}")

