day = int(input("type day: "))
month = int(input("type month: "))

date : tuple[int, int]= (day, month)

daypermonth : list[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

match date:
    # case (g, m) if  g <= 0 or m <= 0:
    #     print("Inserire un valore positivo!")
    case (1, 1):
        print(f"La data {day}/{month} è il Capodanno.")
    case (14, 2):
        print(f"La data {day}/{month} è San Valentino.")
    case (2, 6):
        print(f"La data {day}/{month} è la Festa della Repubblica.")
    case (15, 8):
        print(f"La data {day}/{month} è Ferragosto.")
    case (31, 10):
        print(f"La data {day}/{month} è Halloween.")
    case (25, 12):
        print(f"La data {day}/{month} è il Natale.")
    case (g, m) if m > 12 or g > daypermonth[m-1]:
        print(f"Il {day}/{month} non esiste")
    case _:
        print("Nessuna festività importante in questa data.")
    
