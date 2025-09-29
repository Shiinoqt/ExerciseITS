from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def render(self):
        pass

class Square(Shape):
    def __init__ (self, side_length: float):
        self.shape_name = "Square"
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length
    
    def render(self):
        for i in range(self.side_length):
            if i == 0 or i == self.side_length - 1:
                print('*' * self.side_length)
            else:
                print('*' + ' ' * (self.side_length - 2) + '*')

class Rectangle(Shape):
    def __init__ (self, width: float, height: float):
        self.shape_name = "Rectangle"
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def render(self):
        for i in range(1, self.height + 1):
            # Compute how wide this row should be (scale base across height)
            row_length = round((i / self.height) * self.width)

            if row_length <= 1:
                print("*")  # first row
            elif i == self.height:
                print("*" * self.width)  # last row (full base)
            else:
                print("*" + " " * (row_length - 2) + "*")  # hollow rows

class Triangle(Shape):
    def __init__ (self, base: float, height: float):
        self.shape_name = "Triangle"
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def render(self):
        for i in range(1, self.height + 1):
            # First row (just one star)
            if i == 1:
                print("*")
            # Last row (full base of stars)
            elif i == self.height:
                print("*" * self.base)
            else:
                # Middle rows: one star, spaces, one star
                if i <= self.base:  # avoid too many spaces if base < height
                    print("*" + " " * (i - 2) + "*")

if __name__ == "__main__":
    square = Square(5)
    print(f"Area of the {square.shape_name}: {square.area()}")
    square.render()

    rectangle = Rectangle(10, 4)
    print(f"Area of the {rectangle.shape_name}: {rectangle.area()}")
    rectangle.render()

    triangle = Triangle(12, 12)
    print(f"Area of the {triangle.shape_name}: {triangle.area()}")
    triangle.render()