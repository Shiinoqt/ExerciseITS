class Movie:
    def __init__ (self, movie_id: str, title: str, director: str, is_rented: bool = False):
        self.id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def rent(self) -> None:
        if self.is_rented:
            raise Exception(f"Il film '{self.title}' è già noleggiato.")
        
        self.is_rented = True

    def return_movie(self):
        if self.is_rented:
            self.is_rented = False
        else:
            raise Exception(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")
        
        
class Customer:

    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie] = []):
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = rented_movies
    
    def rent_movie(self, movie: Movie):
        if movie.is_rented == False:
            self.rented_movies.append(movie)
            movie.is_rented = True
        else:
            raise Exception(f"Il film '{movie.title}' è già stato noleggiato.")

    def return_movie(self, movie: Movie):
        if movie not in self.rented_movies: 
            raise Exception(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")
        
        self.rented_movies.remove(movie)


class VideoRentalStore:
    def __init__(self, movies: dict[str, Movie] = {}, customers: dict[str, Customer] = {}):
        self.movies = movies
        self.customers = customers

    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id not in self.movies:
            self.movies[movie_id] = Movie(movie_id, title, director)
        else:
            raise Exception(f"Il film con ID '{movie_id}' esiste già.")
        
    def register_customer(self, customer_id: str, name: str):
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id, name)
        else:
            raise Exception(f"Il cliente con ID '{customer_id}' è gia registrato.")
        
    def rent_movie(self, customer_id: str, movie_id: str):
        # Check if customer or movie exist in the store
        if customer_id not in self.customers:
            raise Exception(f"Il cliente con ID '{customer_id}' non esiste.")
        if movie_id not in self.movies:
            raise Exception(f"Il film con ID '{movie_id}' non esiste.")
        
        # "Creates" an instance of customer in the rental using his id
        customer = self.customers[customer_id]

        # "Creates" an instance of movie in the rental using id
        movie = self.movies[movie_id]

        customer.rent_movie(movie)

    def return_movie(self, customer_id: str, movie_id: str):
        # Check if customer or movie exist in the store
        if customer_id not in self.customers:
            raise Exception(f"Il cliente con ID '{customer_id}' non esiste.")
        if movie_id not in self.movies:
            raise Exception(f"Il film con ID '{movie_id}' non esiste.")
        
        customer = self.customers[customer_id]
        movie = self.movies[movie_id]
        customer.return_movie(movie)

    def get_rented_movies(self, customer_id: str):
        if customer_id not in self.customers:
            raise Exception(f"Il cliente con ID '{customer_id}' non esiste.")
        customer = self.customers[customer_id]
        return customer.rented_movies
        

if __name__ == "__main__":
    # Create a store
    store = VideoRentalStore()
    # Add movies
    store.add_movie("001", "HP", "yuck")
    store.add_movie("002", "HP 2", "yuck")
    # Register customers
    store.register_customer("001", "Pippo")
    store.register_customer("002", "Pluto")

    # Rent movies
    print("Renting movie 001 to Pippo:")
    store.rent_movie("001", "001")
    print("Pippo's rented movies:", [m.title for m in store.get_rented_movies("001")])

    print("Renting movie 002 to Pluto:")
    store.rent_movie("002", "002")
    print("Pluto's rented movies:", [m.title for m in store.get_rented_movies("002")])

    # Try to rent an already rented movie
    try:
        print("Trying to rent already rented movie 001 to Pluto:")
        store.rent_movie("002", "001")
    except Exception as e:
        print("Expected error:", e)

    # Return a movie
    print("Returning movie 001 from Pippo:")
    store.return_movie("001", "001")
    print("Pippo's rented movies after return:", [m.title for m in store.get_rented_movies("001")])

    # Try to return a movie not rented
    try:
        print("Trying to return movie 001 from Pluto (not rented by Pluto):")
        store.return_movie("002", "001")
    except Exception as e:
        print("Expected error:", e)

    # Try to get rented movies for non-existent customer
    try:
        print(store.get_rented_movies("999"))
    except Exception as e:
        print("Expected error:", e)