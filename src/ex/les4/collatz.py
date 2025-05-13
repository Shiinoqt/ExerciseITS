import matplotlib.pyplot as plt

x= int(input("Type number: "))

def Collatz (x):
    if x > 0:
        if x % 2 == 0:
            return print(x / 2)
        else:
            return print(x*3+1)

while x != 1:
    if x == 0:
        break

    print(f"The current number is: {x}")
    
    Collatz(x)
    
    x -= 1




# print(Collatz(x))