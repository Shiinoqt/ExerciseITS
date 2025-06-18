from my_project.weather import check_weather
import pytest

@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (19.99, "cold"),
    (20.00, "hot"),
    (0.00, "cold"),
    (15.00, "average")
])

def test_check_weather(temperature, expected):
    ae: str = ""
    if temperature > 20:
        ae = "temperature greater than 20 must be considered as hot"
    elif 10 < temperature <= 20:
        ae = "temperature between 10 and 20 must be considered as average"
    else:
        ae = "temperature less than or equal to 10 must be considered as cold"
    assert check_weather(temperature) == expected, ae

# def test_check_weather1():
#     assert check_weather(19.99) == "cold", 'temperatures less than 20 degree \
#     must be considered as cold'

# def test_check_weather2():
#     assert check_weather(20.00) == "hot", 'temperatures equal to 20 degree \
#     must be considered as hot'

# def test_check_weather3():
#     assert check_weather(0.00) == "cold", 'temperatures less than 20 degree \
#     must be considered as cold'

# def test_check_weather4():
#     assert check_weather(15.00) == "average", 'temperatures greater than 20 degree \
#     must be considered as average'