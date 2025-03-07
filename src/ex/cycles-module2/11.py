# ex. 11

n = int(input("Type number: "))

if n % 1 == 0:
    if n % 2 == 0 and n > 10:
        print("Number is valid")
    else:
        print("Number isn't valid")
while True:
    n = int(input("Type number: "))
    if n % 1 == 0:
        if n % 2 == 0 and n > 10:
            print("Number is valid")
            break
        else:
            print("Number isn't valid")