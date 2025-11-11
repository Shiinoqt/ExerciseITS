class RecipeManager:
    def __init__ (self) -> None:
        self.recipes: dict[str, list[str]] = {}

    def create_recipe(self, name: str, ingredients: list[str]) -> None:
        if name in self.recipes:
            return "Errore: la ricetta esiste già"
        self.recipes[name] = ingredients

        return {name: ingredients}
    
    def add_ingredient(self, name: str, ingredient: str) -> dict | str:
        if name not in self.recipes or ingredient in self.recipes[name]:
            return "Errore"
        self.recipes[name].append(ingredient)
        return {name: self.recipes[name]}
    
    def remove_ingredient(self, name: str, ingredient: str) -> dict | str:
        if name not in self.recipes or ingredient not in self.recipes[name]:
            return "Errore"
        self.recipes[name].remove(ingredient)
        return {name: self.recipes[name]}
    
    def update_ingredient(self, name: str, old_ingredient: str, new_ingredient: str) -> dict | str:
        if name not in self.recipes or old_ingredient not in self.recipes[name]:
            return "Errore"
        index = self.recipes[name].index(old_ingredient)
        self.recipes[name][index] = new_ingredient
        return {name: self.recipes[name]}
    
    def list_recipes(self):
        return list(self.recipes.keys())
    
    def list_ingredients(self, name: str) -> dict | str:
        if name not in self.recipes:
            return "Errore: la ricetta non esiste."
        return list(self.recipes[name])
    
    def search_recipe_by_ingredient(self, ingredient: str) -> list[str]:
        result = {}
        for name, ingredients in self.recipes.items():
            if ingredient in ingredients:
                result[name] = ingredients
        return result
