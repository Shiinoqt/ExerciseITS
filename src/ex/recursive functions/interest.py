def compoundInterest(m: int, t:int):

    if t == 0:
        return m
    
    else:
        return compoundInterest(m * 1.005, t-1)
        
    

print(compoundInterest(2000, 10))