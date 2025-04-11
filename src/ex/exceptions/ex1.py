import math

def safe_sqrt(x):
    return math.sqrt(x)


x = int(input("Enter a number: "))

try:
    safe_sqrt(x)

except ValueError:
    print("The input value is negative.")