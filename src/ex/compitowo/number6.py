def convert_temperature(temp: float, to_fahrenheit: bool = True) -> float:
    
    #When bool is False we return the temperature in Celsius
    if to_fahrenheit == False:
        temp = (temp-32) * 5/9
        return temp
    
    #Otherwise gets converted to Fahrenheit
    else:
        temp = (temp*9/5) + 32
        return temp