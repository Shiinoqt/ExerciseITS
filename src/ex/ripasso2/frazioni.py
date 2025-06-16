class Frazione:
    def __init__(self, numeratore: int, denominatore: int) -> None:
        if denominatore == 0:
            raise ValueError("Il denominatore non può essere zero.")
        self._numeratore = numeratore
        self._denominatore = denominatore

    def setNumeratore(self, numeratore: int) -> None:
        if isinstance(numeratore, int):
            self._numeratore = numeratore
        else:
            self._numeratore = 13
            self._denominatore = 5

    def setDenominatore(self, denominatore: int) -> None:
        if isinstance(denominatore, int) and denominatore != 0:
            self._denominatore = denominatore
        else:
            raise ValueError("Il denominatore deve essere un intero diverso da zero.")

    def getNumeratore(self) -> int:
        return self._numeratore
    
    def getDenominatore(self) -> int:
        return self._denominatore
    
    def value(self):
        return round(self._numeratore / self._denominatore, 3)
    
    def __str__(self) -> str:
        return f"{self._numeratore}/{self._denominatore}"
    
    def __repr__(self) -> str:
        return f"Frazione({self._numeratore}, {self._denominatore})"
    

def mcd(x: int, y: int) -> int:
    xDiv: list = []
    yDiv: list = []
    result: int = 1

    for i in range(1, x + 1):
        if x % i == 0:
            xDiv.append(i)
    
    for i in range(1, y + 1):
        if y % i == 0:
            yDiv.append(i)

    for i in xDiv:
        if i in yDiv:
            result = i
            
    return result


def semplifica(frazioni: list[Frazione]) -> list[Frazione]:
    frazioni_semplificate = []

    for f in frazioni:
        if isinstance(f, Frazione):
            mcd_value = mcd(f.getNumeratore(), f.getDenominatore())
            numeratore_simplified = f.getNumeratore() // mcd_value
            denominatore_simplified = f.getDenominatore() // mcd_value
            frazioni_semplificate.append(Frazione(numeratore_simplified, denominatore_simplified))

    return frazioni_semplificate

def fractionCompare(frazioni: list[Frazione], frazioni_simplified: list[Frazione]) -> str:
    for i in range(len(frazioni)):
        print(f"Frazione originale: {frazioni[i]} - Valore: {frazioni[i].value()}")
        print(f"Frazione semplificata: {frazioni_simplified[i]} - Valore: {frazioni_simplified[i].value()}")

if __name__ == "__main__":
    f = Frazione(18, 12)
    print(f"Frazione originale: {f}")
    print(f"Valore della frazione: {f.value()}")
    
    f.setNumeratore(24)
    f.setDenominatore(16)
    print(f"Frazione modificata: {f}")
    print(f"Valore della frazione modificata: {f.value()}")

    frazioni = [Frazione(18, 12), Frazione(2, 4), Frazione(5, 11)]
    frazioni_semplificate = semplifica(frazioni)
    print(f"Frazioni semplificate:{frazioni_semplificate.__repr__()}")


    fractionCompare(frazioni, frazioni_semplificate)