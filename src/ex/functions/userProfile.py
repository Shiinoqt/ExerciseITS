def build_profile(name: str, lastname: str, age: int, hair: str, weight: int):
    print(f"{name} {lastname}, age {age}, hair {hair}, weight {weight}")

while True:
    name = str(input("Insert your name: "))
    if name == "quit":
        break
    lastname = str(input("Insert your lastname: "))
    age = int(input("Age: "))
    hair = str(input("Hair color: "))
    weight = int(input("Weight: "))

    build_profile(name, lastname, age, hair, weight)

# build_profile("Pierre","Rebong", 19, "black", 60)