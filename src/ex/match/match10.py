phrase = str(input("Type your phrase: ")).lower()

match phrase[-1]:
    case "?" if len(phrase) % 2 == 0:
        print("Si")
    case "?" if len(phrase) % 2 != 0:
        print("No")
    case "!":
        print("Wow!")
    case _:
        print(f'Tu dici "{phrase}"')
