import string

class Document:

    _text: str

    def __init__(self, text: str = ""):
        self.setText(text)

    def getText(self) -> str:
        return self._text
    
    def setText(self, text: str) -> None:
        if isinstance(text, str):
            self._text = text

    def isInText(self, word: str) -> bool:
        newText = ""

        for char in self._text:
            if char not in string.punctuation:
                newText += char
            else:
                newText += " "

        if word.lower() in newText.lower().split():
            return True
        
        return False
        
class Email(Document):
    
    def __init__(self, mittente: str, destinatario: str, title: str, messaggio: str):
        super().__init__(messaggio)
        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitle(title)

    def setMittente(self, mittente: str) -> None:
        if isinstance(mittente, str):
            self._mittente = mittente

    def setDestinatario(self, destinatario: str) -> None:
        if isinstance(destinatario, str):
            self._destinatario = destinatario

    def setTitle(self, title: str) -> None:
        if isinstance(title, str):
            self._title = title

    def getMittente(self) -> str:
        return self._mittente

    def getDestinatario(self) -> str:
        return self._destinatario
    
    def getTitle(self) -> str:
        return self._title
    
    def getMessaggio(self) -> str:
        return self._text
    
    def getText(self):
        return f"Da: {self.getMittente()}, A: {self.getDestinatario()}\nTitolo: {self.getTitle()}\nMessaggio: {self._text}"
    
    def writeToFile(self, path) -> None:
        with open(path, "w") as f:
            f.write(self.getText())

class File(Document):
    
    def __init__(self, path: str):
        super().__init__()
        self._path = path
        self.readTextFromFile()

    def readTextFromFile(self) -> None:
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                content = f.read()
                self.setText(content)
        except FileNotFoundError:
            print(f"File not found: {self._path}")
            self.setText("")
        except Exception as e:
            print(f"Error reading file: {e}")
            self.setText("")

    def getText(self) -> str:
        return f"Percorso: {self._path}\nContenuto: {self._text}"
    
if __name__ == "__main__":

    test1 = Document("Ciaone, sono Pierone.")
    print(f"{test1.getText()}") 
    print(test1.isInText("Ciaone")) 
    print(test1.isInText("Pierone"))  
    print(f"\n")

    email1 = Email("alice@example.com", "bob@example.com", "Incontro", "Ciao Bob, possiamo incontrarci domani?")
    print(email1.getMittente())
    print(email1.getDestinatario())
    print(email1.getMessaggio())
    print(f"\n")
    print(email1.getText())
    
    email1.writeToFile("/home/damien/Documents/ExerciseITS/src/ex/lez21/testo.txt")
    
    print(f"\n")
    file1 = File("/home/damien/Documents/ExerciseITS/src/ex/lez21/document.txt")
    print(file1.getText())