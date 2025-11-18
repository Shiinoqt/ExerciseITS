from abc import ABC, abstractmethod
from flask import Flask

class Ride(ABC):
    @abstractmethod
    def __init__(self, id: str, name: str, min_height_cm: int):
        self.id = id
        self.name = name
        self.min_height_cm = min_height_cm

    @abstractmethod
    def category(self) -> str:
        pass

    @abstractmethod
    def base_wait(self) -> int:
        pass

    @abstractmethod
    def info(self) -> str:
        pass

    def wait_time(self, crowd_factor: float = 1.0) -> int:
        return int(self.base_wait() * crowd_factor)
    

class RollerCoaster(Ride):
    def __init__(self, id: str, name: str, min_height_cm: int, inversions: int):
        super().__init__(id, name, min_height_cm)
        self.inversions = inversions

    def category(self) -> str:
        return "roller_coaster"

    def base_wait(self) -> int:
        return 30 + (self.inversions * 5)

    def info(self) -> str:
        return f"{self.name} (Inversions: {self.inversions})"
    

class Carousel(Ride):
    def __init__ (self, id: str, name: str, min_height_cm: int, animals: list[str]):
        super().__init__(id, name, min_height_cm)
        self.animals = animals

    def category(self) -> str:
        return "family"
    
    def base_wait(self):
        return 10
    
    def info(self):
        return f"{self.name} (Animals: {', '.join(self.animals)})"
    

class Park:
    def __init__ (self, rides: list[Ride] | None = None):
        self.rides = rides or []

    def add(self, ride: Ride):
        self.rides.append(ride)

    def get(self, id: str) -> Ride | None:
        for ride in self.rides:
            if ride.id == id:
                return ride
        return None
    
    def list_all(self) -> list[str]:
        return [ride.info() for ride in self.rides]
    

if __name__ == "__main__":
    park = Park()

    rc1 = RollerCoaster("rc1", "Thunderbolt", 120, 3)
    car1 = Carousel("car1", "Merry-Go-Round", 0, ["horse", "lion", "elephant"])

    park.add(rc1)
    park.add(car1)

    print(park.list_all())


app = Flask(__name__)