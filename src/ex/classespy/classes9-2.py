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
restaurant2 = Restaurant("KFC", "Fast Food")
restaurant3 = Restaurant("Burger King", "Fast Food")


print(restaurant.name)
print(restaurant.cuisine)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()