
from film import Film
from noleggio import Noleggio
from movie_genre import Action, Comedy, Drama

if __name__ == "__main__":
    # Crea 5 film d'azione
    action_movie1 = Action()
    action_movie1.setId("A1")
    action_movie1.setTitle("Mission Impossible")
    action_movie2 = Action()
    action_movie2.setId("A2")
    action_movie2.setTitle("Warrior")
    action_movie3 = Action()
    action_movie3.setId("A3")
    action_movie3.setTitle("Gladiator")
    action_movie4 = Action()
    action_movie4.setId("A4")
    action_movie4.setTitle("Mad Max")
    action_movie5 = Action()
    action_movie5.setId("A5")
    action_movie5.setTitle("John Wick")

    action_movies = [action_movie1, action_movie2, action_movie3, action_movie4, action_movie5]

    # Crea 4 commedie
    comedy_movie1 = Comedy()
    comedy_movie1.setId("C1")
    comedy_movie1.setTitle("The Hangover")
    comedy_movie2 = Comedy()
    comedy_movie2.setId("C2")
    comedy_movie2.setTitle("Superbad")
    comedy_movie3 = Comedy()
    comedy_movie3.setId("C3")
    comedy_movie3.setTitle("Step Brothers")
    comedy_movie4 = Comedy()
    comedy_movie4.setId("C4")
    comedy_movie4.setTitle("Anchorman")

    comedy_movies = [comedy_movie1, comedy_movie2, comedy_movie3, comedy_movie4]

    # Crea 1 film drammatico
    drama_movie = Drama()
    drama_movie.setId("D1")
    drama_movie.setTitle("The Shawshank Redemption")

    # Lista totale film
    film_list = action_movies + comedy_movies + [drama_movie]

    # Crea oggetto Noleggio
    noleggio = Noleggio(film_list)

    print("Quale film vuoi nolleggiare?")

    # Simula il noleggio di un film da parte del primo cliente
    client1 = "Mario Rossi"
    client2 = "Luigi Bianchi"
    film1 = action_movies[0]
    noleggio.rentAMovie(film1, client1)

    # Simula il noleggio di un secondo film da parte del primo cliente
    film2 = comedy_movies[0]
    noleggio.rentAMovie(film2, client1)

    # Simula il tentativo di noleggio dello stesso film da parte del secondo cliente
    noleggio.rentAMovie(film2, client2)

    # Simula il noleggio di un terzo film da parte del secondo cliente
    film3 = action_movies[1]
    noleggio.rentAMovie(film3, client2)

    # Simula il reso del secondo film noleggiato dal primo cliente
    noleggio.giveBack(film2, client1, days=3)

    # Stampa la lista dei film disponibili in negozio
    print("\nFilm disponibili in negozio:")
    noleggio.printMovies()