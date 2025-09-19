class Film:
    def __init__ (self, id: str, title: str) -> None:
        self.__id = id
        self.__title = title

    def getId(self) -> str:
        return self.__id
    
    def setId(self, id: str) -> None:
        self.__id = id
    
    def getTitle(self) -> str:
        return self.__title

    def setTitle(self, title: str) -> None:
        self.__title = title

    def isEqual(self, otherFilm: 'Film') -> bool:
        return self.__id == otherFilm.getId() and self.__title == otherFilm.getTitle()
    
    