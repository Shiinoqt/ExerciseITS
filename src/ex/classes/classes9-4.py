class Restaurant:
    def __init__(self, name, cuisine, number_served):
        self.name = name
        self.cuisine = cuisine
        self.served = number_served

    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine)
        print(self.served)

    def open_restaurant(self):
        print(f"{self.name} is open!")
    
    def set_number_served(self, number):
        self.served = number
        


restaurant = Restaurant("McDonald","Fast Food", 0)

print(restaurant.name)
print(restaurant.cuisine)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("---"*20)

restaurant.set_number_served(12)
restaurant.describe_restaurant()




