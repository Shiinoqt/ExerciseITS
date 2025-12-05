from abc import ABC, abstractmethod
from flask import Flask, jsonify, url_for

class Animal(ABC):
    @abstractmethod
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float) -> None:
        self.id = id
        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg

    @abstractmethod
    def species(self) -> str:
        pass

    @abstractmethod
    def daily_food_grams(self) -> int:
        pass

    def info(self) -> dict:
        return {"id": self.id, "name": self.name, "species": self.species(), "age_years": self.age_years, "weight_kg": self.weight_kg}
    
    def bmi_like(self) -> float:
        return self.weight_kg / (self.age_years + 1)
    
class Dog(Animal):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, breed: str, is_trained: bool) -> None:
        super().__init__(id, name, age_years, weight_kg)
        self.breed = breed
        self.is_trained = is_trained

    def species(self) -> str:
        return 'dog'
    
    def daily_food_grams(self) -> int:
        return 200 + self.age_years * 50
    
    def info(self) -> dict:
        return {"id": self.id, "name": self.name, "species": self.species(), "age_years": self.age_years, "weight_kg": self.weight_kg, "breed": self.breed, "is_trained": self.is_trained}

class Cat(Animal):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, indoor_only: bool, favorite_toy: str) -> None:
        super().__init__(id, name, age_years, weight_kg)
        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy

    def species(self) -> str:
        return 'cat'
    
    def daily_food_grams(self) -> int:
        return 100 + self.age_years * 30
    
    def info(self) -> dict:
        return {"id": self.id, "name": self.name, "species": self.species(), "age_years": self.age_years, "weight_kg": self.weight_kg, "indoor_only": self.indoor_only, "favorite_toy": self.favorite_toy}
    
class Shelter:
    def __init__(self, animals: dict | None = None, adoptions: dict | None = None) -> None:
        self.animals = animals or {}
        self.adoptions = adoptions or {}

    def add(self, animal: Animal) -> None:
        if animal.id not in self.animals:
            self.animals[animal.id] = animal

    def get(self, animal_id: str) -> Animal | None:
        return self.animals.get(animal_id)

    def list_all(self) -> list:
        return [animal.info() for animal in self.animals.values()]

    def is_adopted(self, animal_id: str) -> bool:
        return animal_id in self.adoptions

    def set_adopted(self, animal_id: str, adopter_name: str) -> None:
        if animal_id in self.animals:
            self.adoptions[animal_id] = adopter_name
            del self.animals[animal_id]


# Test: Create animals and shelter
if __name__ == "__main__":
    # Create a shelter
    shelter = Shelter()
    
    # Create a dog
    dog = Dog(id="d1", name="Rex", age_years=5, weight_kg=25.0, breed="Labrador", is_trained=True)
    
    # Create a cat
    cat = Cat(id="c1", name="Whiskers", age_years=3, weight_kg=4.5, indoor_only=True, favorite_toy="ball")
    
    # Add animals to shelter
    shelter.add(dog)
    shelter.add(cat)
    
    app = Flask(__name__)

    @app.route('/', methods=["GET"])
    def home():
        links = {
           "list_animals": url_for("list_animals"),
           "sample_dog": url_for("get_animal", animal_id="d1") 
        }

        return jsonify({
            "message": "Welcome to Animal Shelter API",
            "links": links
        })
    
    @app.route('/animals', methods=['GET'])
    def list_animals():
        return jsonify(shelter.list_all())

    @app.route('/animal/<animal_id>', methods=['GET'])
    def get_animal(animal_id):
        animal = shelter.get(animal_id)
        if animal is None:
            return jsonify({'error': 'not found'}), 404
        return jsonify(animal.info())

    if __name__ == "__main__":
        app.run(debug=True)



