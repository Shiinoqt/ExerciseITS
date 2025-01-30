sum = 0
i = 1
n = int(input("Insert number: "))

if n > 0:
    while i <= n:
        sum += i * i
        i += 1
else:
    print("Error")

print(f"The result is: {sum}")