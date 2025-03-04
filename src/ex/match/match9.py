from random import randint

head : int = 0
tails : int = 0

#iterate 8 flips
for flips in range(1, 9):

    #random result 1 or 2
    coinflip = randint(1, 2)

    #assigning each result to a letter and updating their counter
    match coinflip:
        case 1:
            print(f"Lancio {flips}: T")
            head += 1
        case 2:
            print(f"Lancio {flips}: C")
            tails += 1

#formula
headPer : float = (head/8) * 100
tailsPer : float = (tails/8) * 100

#output results
print(f"\nHeads total: {head}")
print(f"{headPer:.2f}%")

print(f"Tails total: {tails}")
print(f"{tailsPer:.2f}%")




