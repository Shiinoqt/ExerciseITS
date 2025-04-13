def make_car(manufacturer, model, **carInfo):

    #Adds to the dictionary carInfo the keys manufacturer and model
    carInfo['manufacturer'] = manufacturer
    carInfo['model'] = model

    #Returns the dictionary with all the info
    return carInfo


cars = make_car("Tesla", "Model S", color = "blue", tow_package = True)

print(cars)

# if __name__ == "__main__":
#     def make_car(**carInfo):
#         return carInfo

#     cars = make_car(manufacturer = "Tesla", model = "Model S", color = "blue", tow_package = True)

#     print(cars)
