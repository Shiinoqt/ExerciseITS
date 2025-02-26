grade = int(input("Inserisci voto di laurea: "))

match grade:
    case grade if grade >= 106 and grade <= 110:
        print("GPA 4.0")
    case grade if grade >= 101 and grade <= 105:
        print("GPA 3.7")
    case grade if grade >= 96 and grade <= 100:
        print("GPA 3.3")
    case grade if grade >= 91 and grade <= 95:
        print("GPA 3.0")
    case grade if grade >= 86 and grade <= 90:
        print("GPA 2.7")
    case grade if grade >= 81 and grade <= 85:
        print("GPA 2.3")
    case grade if grade >= 76 and grade <= 80:
        print("GPA 2.0")
    case grade if grade >= 70 and grade <= 75:
        print("GPA 1.7")
    case grade if grade >= 66 and grade <= 69:
        print("GPA 1.0")
    case _:
        print("Voto non valido")
