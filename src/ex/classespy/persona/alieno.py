class Alieno:
    def __init__ (self, galaxy:str):
        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy:str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            raise ValueError("Galaxy cannot be empty")
        
    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print(f"Hello, I am an alien from the {self.getGalaxy()} galaxy!")

    def __str__(self) -> str:
        return f"Alieno dalla galassia: {self.getGalaxy()}"

# alien = Alieno("Milky Way")
# print(alien.galaxy)

# alien.setGalaxy("Andromeda")
# print(alien.galaxy)

# alien.speak()