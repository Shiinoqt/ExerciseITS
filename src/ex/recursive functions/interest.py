def compoundInterest(m: int, t:int):

    if t == 0:
        return m
    
    else:
        return round(compoundInterest(m * 1.005, t-1), 2)
    
print(compoundInterest(1000, 3))