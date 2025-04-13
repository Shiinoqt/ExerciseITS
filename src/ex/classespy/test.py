class Persona:
    #self is used to remember their address in memory
    def __init__(self, nome, cognome, eta):

        self.nome = nome 
        self.cognome = cognome
        self.eta = eta

    #Retrieves the name for the set
    def get_nome(self):

        return self.nome
        return self.__nome  #Makes it more private
    
    #Allows to change name using this function because it's written inside the class
    def set_nome(self, nome):

        self.nome = nome
        
    

persona_1: Persona = Persona("Mario","Rossi",30)
persona_2: Persona = Persona("Mario","Rossi",30)
persona_3: Persona = Persona("Mario","Rossi",30)
persona_4: Persona = Persona("Mario","Rossi",30)

