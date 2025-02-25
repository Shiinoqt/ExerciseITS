num1 = int(input("type num 1: "))
num2 = int(input("type num 2: "))
i = 0
multiplier = 1
if num1 > num2:
    for i in range(num2-1, num1+1):
        prod = i*multiplier
        multiplier += 1
else:
    for i in range(num1-1, num2+1):
        prod = i*multiplier
        multiplier += 1  
print(prod)