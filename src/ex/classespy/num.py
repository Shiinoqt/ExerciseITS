class Number:
    def __init__ (self, value):
        self.value = value

    def __eq__ (self, other):
        return self.value == other.value
    
    def __hash__ (self):
        return hash((self.value))

x: Number = Number(5)
y: Number = Number(4)
z: Number = Number("Holon")

print(Number.__eq__(x, y))
print(Number.__hash__(z))

print(hash(z))

print(hash("Popa"))