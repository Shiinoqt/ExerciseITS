name = str(input("Insert name: "))
gender = str(input("Insert gender: "))

match (gender.lower()):
    case ("m"):
        print(f"Name: {name} \nGender: Male")
    case ("f"):
        print(f"Name: {name} \nGender: Female")
    case _:
        print("Non è possibile generare documento di identità")