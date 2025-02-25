num = 0
maxN = num
minN = num
tot = 0
i = 1
while True:
    num = float(input("Type number: "))
    if num.is_integer() and num > 0:
        tot = tot + num
        media = tot / i
        i += 1
    if num > maxN:
        maxN = num
        minN = num
    if num < minN:
        minN = num
    print(f"The average is: {media}")
    print(f"The biggest number now is: {maxN}")
    print(f"The smallest number now us: {minN}")
    if num < 0:
        break

