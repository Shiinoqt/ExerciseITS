class Persona:
    
    # Constructor of the class Persona  
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0

    # Method to display the data of the instance
    def displayData(self) -> None:
        print(f"Name: {self.name}, Last Name: {self.lastname}, Age: {self.age}")

    #  Method to set the name of the instance
    def setName(self, name:str) -> None:
        self.name = name

    # Method to set the surname of the instance
    def setLastname(self, lastname:str) -> None:
        self.lastname = lastname

    # Method to set the age of the instance
    def setAge(self, age:int) -> None:
        if age < 0 or age > 120:
            self.age = 0

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

# Creates a new instance of the class Persona
fm = Persona()

# Sets the name of the instance fm
fm.setName("Francesco")

# Sets the surname of the instance fm
fm.setLastname("Mazzola")

# Sets the age of the instance fm
fm.setAge(25)

# Displays the data of the instance fm
fm.displayData()



# Gets the name of the instance fm
print(fm.getName()) 

# Gets the surname of the instance fm
print(fm.getLastname())

# Gets the age of the instance fm
print(fm.getAge())