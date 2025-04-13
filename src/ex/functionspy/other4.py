def describe_city(city:str, country:str = "Italy"):
    print(f"{city} is in {country}.")

describe_city("Rome")
describe_city("Milan")
describe_city("Berlin","Germany")