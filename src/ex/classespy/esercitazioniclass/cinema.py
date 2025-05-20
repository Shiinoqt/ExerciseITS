class Film:
    def __init__ (self, titolo: str, durata: int) -> None:
        self.titolo = titolo
        self.durata = durata

    def getTitolo (self) -> str:
        return self.titolo

    def getDurata (self) -> int:
        return self.durata

class Sala:
    def __init__ (self, id: int, film_programmato: Film, posti_totali: int) -> None:
        self.id = id
        self.film_programmato = film_programmato
        self.posti_totali = posti_totali

    def getId (self) -> int:
        return self.id
    
    def getFilm (self) -> Film:
        return self.film_programmato

    def prenota_posti (self, num_posti: int) -> None:
        if self.posti_totali >= num_posti:
            self.posti_totali -= num_posti
        else:
            raise ValueError("Posti non disponibili")
        
    def getPosti_disponibili (self) -> int:
        return self.posti_totali
    
class Cinema:
    def __init__(self):
        self.sale = []

    def aggiungi_sala(self, sala: Sala) -> None:
        self.sale.append(sala)

    def prenota_film(self, titolo: str, num_posti: int) -> None:
        for sala in self.sale:
            if sala.film_programmato.titolo == titolo:
                sala.prenota_posti(num_posti)
                return
        raise ValueError("Film non trovato")


if __name__ == "__main__":
    # Esempio di utilizzo
    film = Film("Inception", 148)
    film2 = Film("Interstellar", 169)

    sala1 = Sala(1, film, 100)
    sala2 = Sala(2, film2, 50)

    cinema = Cinema()
    cinema.aggiungi_sala(sala1)
    cinema.aggiungi_sala(sala2)

    # Prenotazione posti
    print(f"Film in sala 1: {sala1.film_programmato.titolo}, Posti disponibili: {sala1.getPosti_disponibili()}")
    print(f"Film in sala 2: {sala2.film_programmato.titolo}, Posti disponibili: {sala2.getPosti_disponibili()}")

    # Prenotazione film
    cinema.prenota_film("Inception", 5)
    cinema.prenota_film("Interstellar", 10)

    print(f"Film in sala 1: {sala1.film_programmato.titolo}, Posti disponibili: {sala1.getPosti_disponibili()}")
    print(f"Film in sala 2: {sala2.film_programmato.titolo}, Posti disponibili: {sala2.getPosti_disponibili()}")

