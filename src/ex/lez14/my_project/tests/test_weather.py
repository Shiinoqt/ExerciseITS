from my_project.weather import check_weather

def test_check_weather():
    assert check_weather(21.00) == "hot", 'temperatures greater than 20 degree \
    must be considered as hot'