import json

PATH: str = "Exercise/src/ex/les15/config2.json"
mode: str = "r"
encoding: str = "utf-8"

config: dict = {"Codice Fiscale": {"name": "Mario", "surname": "Rossi", "birthdate": "01/01/1990", "place_of_birth": ""}}

with open(PATH, mode= "w") as file:

    json.dump(config, file, indent=4)