def serie(target: str = "3.14"):

    pi: float = 0.0
    segno: int = 1
    denominatore: int = 1
    contatore: int = 0

    while True:
        
        pi += segno * (4 / denominatore)

        if str(pi)[:len(target)] == target:

            print(f"π ≈ {pi} dopo {contatore} iterazioni")
            
            break


        segno *= -1
        denominatore += 2
        contatore += 1

serie()