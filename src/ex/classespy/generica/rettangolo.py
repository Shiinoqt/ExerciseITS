from formagenerica import FormaGenerica

class Rettangolo(FormaGenerica):
    def __init__(self) -> None:
        super().__init__()
        self.setShape("Rettangolo")
    
    def draw(self) -> None:
        print(f"Drawing a {self.getShape()}")
        for i in range(5):
            for j in range(10):
                if i == 0 or i == 5-1:
                    print("* ", end="")

                elif j == 0 or j == 10-1:
                    print("* ", end="")

                else:
                    print("  ", end="")

            print("\n", end="")
