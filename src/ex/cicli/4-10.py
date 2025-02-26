pizza = ["Margherita","Diavola","Boscaiola","Bianca"]

x = slice(0, 3)
y = slice(1, -1)
z = slice(-1, -4, -1)

print(f"The first three items are: {pizza[x]}")
print(f"The first three items are: {pizza[y]}")
print(f"The last three items: {pizza[z]}")