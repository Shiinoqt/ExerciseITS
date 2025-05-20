class Prodotto:
    def __init__ (self, nome: str, quantita: int) -> None:
        self.nome = nome
        self.quantita = quantita

    def getNome (self) -> str:
        return self.nome
    
    def getQuantita (self) -> int:
        return self.quantita
    
    def setQuantita (self, quantita: int) -> None:
        if quantita < 0:
            raise ValueError("La quantità non può essere negativa")
        self.quantita = quantita

    def aggiungiQuantita (self, quantita: int) -> None:
        if quantita < 0:
            raise ValueError("La quantità da aggiungere non può essere negativa")
        self.quantita += quantita


class Magazzino:
    def __init__ (self) -> None:
        self.prodotti = []

    def aggiungi_prodotto (self, prodotto: Prodotto) -> None:
        self.prodotti.append(prodotto)

    def cerca_prodotto (self, nome: str) -> Prodotto:
        for prodotto in self.prodotti:
            if prodotto.nome == nome:
                return prodotto
        raise ValueError("Prodotto non trovato")
    
    def verifica_disponibilita (self, nome: str, quantita: int) -> bool:
        try:
            prodotto = self.cerca_prodotto(nome)
            return prodotto.quantita >= quantita
        except ValueError:
            return False


if __name__ == "__main__":
    # Esempio di utilizzo
    magazzino = Magazzino()
    
    prodotto1 = Prodotto("Mela", 50)
    prodotto2 = Prodotto("Banana", 30)
    
    magazzino.aggiungi_prodotto(prodotto1)
    magazzino.aggiungi_prodotto(prodotto2)
    
    # Verifica disponibilità
    print(magazzino.verifica_disponibilita("Mela", 20))  # True
    print(magazzino.verifica_disponibilita("Banana", 40))  # False