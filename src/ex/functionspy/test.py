boh : list[int] = [1, 2, 3]
print(boh)
print(*boh)

mytuple : tuple[int] = (1, 2, 3, 4, 5)
print(mytuple)
print(*mytuple)

def greet(name:str, message:str = "Welcome") -> None:
    print(f"Hi {name}, {message}")

greet("Mike")