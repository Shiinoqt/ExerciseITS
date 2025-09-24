from movie_genre import *


class Noleggio:
    def __init__(self, film_list: list[Film]):
        self.film_list = film_list
        self.rented_film = {}

    def isAvailable(self, film: Film) -> bool:
        for f in self.film_list:
            if f.isEqual(film):
                print(f"Il film scelto è disponibile: {film.getTitle()}!")
                return True
        print(f"Il film scelto non è disponibile: {film.getTitle()}!")
        return False

    def rentAMovie(self, film: Film, clientID: str) -> None:
        if self.isAvailable(film):
            self.film_list = [f for f in self.film_list if not f.isEqual(film)]
            if clientID not in self.rented_film:
                self.rented_film[clientID] = []
            self.rented_film[clientID].append(film)
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile noleggiare il film {film.getTitle()}!")

    def giveBack(self, film: Film, clientID: str, days: int) -> None:
        if clientID in self.rented_film and film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            self.film_list.append(film)
            penalty = film.getLatePenalty(days)
            print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} e' di {penalty} euro!")
        else:
            print(f"Il film {film.getTitle()} non è stato trovato tra quelli noleggiati dal cliente {clientID}.")

    def printMovies(self) -> None:
        for film in self.film_list:
            print(f"{film.getTitle()} - {film.getGenre()}")

    def printRentMovies(self, clientID: str) -> None:
        if clientID in self.rented_film and self.rented_film[clientID]:
            for film in self.rented_film[clientID]:
                print(f"{film.getTitle()} - {film.getGenre()}")
        else:
            print(f"Nessun film noleggiato dal cliente {clientID}.")
