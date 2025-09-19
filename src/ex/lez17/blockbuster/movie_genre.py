from film import Film

class Action(Film):
    __genre: str = "Action"
    __penalty: float = 3.00
    
    def __init__ (self) -> None:
        super().__init__("", "")

    def getGenre(self) -> None:
        return self.__genre
    
    def getPenalty(self) -> None:
        return self.__penalty
    
    def getLatePenalty(self, days: int) -> None:
        return days * self.getPenalty()

class Comedy(Film):
    __genre: str = "Comedy"
    __penalty: float = 2.50

    def __init__ (self) -> None:
        super().__init__("", "")

    def getGenre(self) -> None:
        return self.__genre
    
    def getPenalty(self) -> None:
        return self.__penalty
    
    def getLatePenalty(self, days: int) -> None:
        return days * self.getPenalty()

class Drama(Film):
    __genre: str = "Drama"
    __penalty: float = 2.00

    def __init__ (self) -> None:
        super().__init__("", "")

    def getGenre(self) -> None:
        return self.__genre
    
    def getPenalty(self) -> None:
        return self.__penalty
    
    def getLatePenalty(self, days: int) -> None:
        return days * self.getPenalty()
    
