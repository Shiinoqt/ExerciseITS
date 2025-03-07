from random import randint

points = 0

while True:
    inp = str(input("Roll the dices?: "))
    if inp.lower() == "yes":
        roll1 = randint(1, 6)
        roll2 = randint(1, 6)
        print(f"Your rolls are {roll1} and {roll2}")
        rollSum = roll1 + roll2
        if (roll1 % 2 == 0 and roll2 % 2 == 0) and rollSum >= 8:
            points = 100
            print("You won the game!")
            break
        elif roll1 == 6 or roll2 == 6 or rollSum == 7:
            points += 10
            print(f"Your points are {points}")
        else: 
            points = 0
            print("You lost!")
            break
    elif inp.lower() == "no":
        break
status = False
print(f"Your score is {points}")