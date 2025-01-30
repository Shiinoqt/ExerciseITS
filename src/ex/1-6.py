x = int(input("Input number: "))
if x > 0:
    i = 1 
    sum = 0
    while i <= 10:
        n = int(input(f"Insert 10 numbers {i}: "))
        if n % 2 == 0:
            if n > (x/2):
                sum = sum + n
        elif n < x:
            sum = sum + n
        i = i + 1
    print(sum)
else:
    print("Error")