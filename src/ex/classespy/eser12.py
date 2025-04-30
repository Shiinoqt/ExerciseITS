class MovieCatalog:
    def __init__(self) -> None:
        self.setCatalog()
    
    def setCatalog(self) -> None:
        self.catalog: dict[str, list[str]] = {}
    
    def getCatalog(self) -> dict[str, list[str]]:
        return self.catalog
    
    def addMovie(self, director: str, movies: list[str]) -> None:
        if director not in self.catalog:
            self.catalog[director] = []
        self.catalog[director].extend(movies)
        self.catalog[director] = list(set(self.catalog[director]))

    def removeMovie(self, director: str, movie: str) -> None:
        if director in self.catalog and movie in self.catalog[director]:
            self.catalog[director].remove(movie)
            if not self.catalog[director]:
                del self.catalog[director]

    def getMovies(self, director: str) -> list[str]:
        if director in self.catalog:
            return self.catalog[director]
        else:
            return []
    
    def searchMovieTitle(self, title: str) -> list[str]:
        result = []
        for director, movies in self.catalog.items():
            if title in movies:
                result.append(title)
        return result
    
    def listDirectors(self) -> list[str]:
        return sorted(self.catalog.keys())
    

# Example usage
if __name__ == "__main__":
    catalog = MovieCatalog()
    catalog.addMovie("Christopher Nolan", ["Inception", "Interstellar"])
    catalog.addMovie("Steven Spielberg", ["Jurassic Park", "E.T."])
    catalog.addMovie("Christopher Nolan", ["Dunkirk"])
    
    print(catalog.getCatalog())
    print(catalog.getMovies("Christopher Nolan"))
    print(catalog.searchMovieTitle("Inception"))
    print(catalog.listDirectors())
    print(f"\n")

    # Removing a movie
    catalog.removeMovie("Christopher Nolan", "Inception")
    print(catalog.getCatalog())
    print(catalog.getMovies("Christopher Nolan"))
    print(catalog.searchMovieTitle("Inception"))
    print(catalog.listDirectors())
    print(f"\n")

    # Removing a director
    catalog.removeMovie("Christopher Nolan", "Dunkirk")
    print(catalog.getCatalog())
    print(catalog.getMovies("Christopher Nolan"))
    catalog.removeMovie("Christopher Nolan", "Interstellar")
    print(catalog.getCatalog())
    print(catalog.getMovies("Christopher Nolan"))
