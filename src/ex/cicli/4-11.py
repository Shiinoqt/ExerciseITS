pizza = ["Margherita","Diavola","Boscaiola","Bianca"]

friend_pizzas = pizza[:]

pizza.append("Prosciutto")
friend_pizzas.append("Carbonara")

print("My favorite pizzas are: ")
for element in pizza:
    print(f"- {element}")

print("My friend's favorite pizzas are: ")
for element in friend_pizzas:
    print(f"- {element}")