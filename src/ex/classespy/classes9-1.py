class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine)

    def open_restaurant(self):
        print(f"{self.name} is open!")


restaurant = Restaurant("McDonald","Fast Food")

print(restaurant.name)
print(restaurant.cuisine)

restaurant.describe_restaurant()

restaurant.open_restaurant()
