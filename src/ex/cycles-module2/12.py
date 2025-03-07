# ex. 12
n = int(input("Type number: "))
i = 1
for i in range(n):
    x = int(input("Type x: "))
    y = int(input("Type b: "))
    if x > 0 and y > 0:
        print(x*y)
    elif x < 0 and y < 0:
        print("Error")
    else:
        print(x-y)