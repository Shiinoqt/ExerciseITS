babies = int(input("Type number of babies: "))

match babies:
    case 1:
        print("Congratulations!")
    case 2: 
        print("Wow! Twins!")
    case 3:
        print("Wow! Triplets!")
    case 4:
        print("Mamma mia quadruplets! Wow!")
    case 5:
        print("Incredible! Quintuplets!")
    case _:
        print(f"Unbelievable! {babies} babies!")