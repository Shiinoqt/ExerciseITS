def integerPower(base: int, exponent: int) -> int:
    result = 1
    
    for i in range(exponent):
        result *= base
        
    return result