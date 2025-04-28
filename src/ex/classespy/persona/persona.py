class Persona:

    # Constructor of the class Persona
    def __init__ (self, name:str, cognome:str, eta:int): 
        self.name = name
        self.cognome = cognome
        self.eta = eta

    # String representation of the class
    def __str__(self) -> str:
        return f"Nome: {self.name}\nCognome: {self.cognome}\nEta: {self.eta}"
        
    #  Method to set the name of the instance
    def setName(self, name:str) -> None:
        self.name = name

    # Method to set the surname of the instance
    def setLastname(self, lastname:str) -> None:
        self.lastname = lastname

    # Method to set the age of the instance
    def setAge(self, age:int) -> None:
        self.age = age

    # Method to get the name of the instance
    def getName(self) -> str:
        return self.name
    
    # Method to get the surname of the instance
    def getLastname(self) -> str:
        return self.lastname
    
    # Method to get the age of the instance
    def getAge(self) -> int:
        return self.age 

    def speak(self) -> None:
        print(f"Hello, my name is {self.getName()}!")

# Creates a new instance of the class Persona
# fm = Persona("Francesco", "Mazzola", 25)

# Displays the data of the instance fm
# fm.displayData()