i = 0
numbers = []
while i < 5:
    num = int(input("Type number: "))
    if num.is_integer and num >= 1 and num <= 30:
        numbers.append(num)
        i += 1
    else:
        print("Deve essere compreso tra 1 e 30!")
for n in numbers:
    print(n*"*")