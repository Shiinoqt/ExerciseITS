def converter(numbers: list) -> dict:

    dizionario: dict = {"Positivi": [], "Negativi": []}

    for number in numbers:
        if number >= 0:
            dizionario["Positivi"].append(number)
        else:
            dizionario["Negativi"].append(number)

    return dizionario

print(converter((0,1,2,-3,-4,5,-6,7,8,-9,10)))