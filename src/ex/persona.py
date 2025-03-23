class Persona:

    # Constructor of the class Persona
    def __init__ (self, nome:str, cognome:str, eta:int): 
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    # Method to display the data of the instance
    def displayData(self) -> None:
        print(f"Nome: {self.nome}, Cognome: {self.cognome}, Eta: {self.eta}")
        


# Creates a new instance of the class Persona
fm = Persona("Francesco", "Mazzola", 25)

# Displays the data of the instance fm
fm.displayData()