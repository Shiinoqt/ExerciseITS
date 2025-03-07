n = int(input("How many numbers you want to insert: ")).is_integer()

i = 1

somma = 0

media = 0

even = 0
odd = 0

while i <= n:
    x = int(input(f"Type number {i}: ")).is_integer()

    somma += x
    media = somma / i

    if x % 2 == 0 and x > media:
        even += x
    elif x < media and x % 2 != 0:
        odd += x
    i += 1

print(even, odd)
