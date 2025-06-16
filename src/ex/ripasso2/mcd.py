def mcd(x: int, y: int) -> int:
    xDiv: list = []
    yDiv: list = []
    result: int = 1

    for i in range(1, x + 1):
        if x % i == 0:
            xDiv.append(i)
    
    for i in range(1, y + 1):
        if y % i == 0:
            yDiv.append(i)

    for i in xDiv:
        if i in yDiv:
            result = i
            
    return result
        
print(mcd(18, 12))
