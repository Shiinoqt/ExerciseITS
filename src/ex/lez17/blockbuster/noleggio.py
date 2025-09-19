from movie_genre import *

class Noleggio:
    __films: list[Film]
    __rentedFilms: dict[Film]

    def __init__(self, films: list[Film]) -> None:
        self.__films = films
        self.__rentedFilms = {}

    def isAvailable(self, film: Film) -> bool:
        for f in self.__films:
            if f.isEqual(film):
                print(f"The chosen film is available for rent. {film.getTitle()}")
                return True 
            
        print(f"The chosen film is not available for rent. {film.getTitle()}")
        return False
    
    def rentFilm(self, film: Film, clientID: str) -> None:
        if self.isAvailable(film):
            self.__rentedFilms[film] = clientID
            print(f"Film rented successfully. {film.getTitle()} to client {clientID}")
        else:
            print(f"Film rental failed. {film.getTitle()} is not available.")
