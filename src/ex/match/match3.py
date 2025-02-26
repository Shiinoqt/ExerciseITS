grade = int(input("Insert grade: "))

match grade:
    case 10:
        print("Excellent!")
    case 8|9:
        print("Great")
    case 6|7:
        print("Good")
    case 4|5:
        print("Insufficient")
    case 1|3:
        print("Gravemente insufficiente")
    case _:
        print("Voto non valido")