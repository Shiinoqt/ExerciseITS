import random
import time

x = "_"
#List of the turtle's track
trackTurtle = ["T"] + [x]*70

#List of the hare's track
trackHare = ["H"] + [x]*70
# print(trackTurtle)


def TurtleMove():

    move = random.randint(1, 10)
    # print(f"è uscito: {move}")

    # currentPos = trackTurtle.index("T")
    # print(currentPos)

    currentPos = trackTurtle.index("T")
    # print(f"La posizione adesso è: {currentPos}")

    #50% chance
    if move >= 1 and move <= 2:

        trackTurtle.pop(currentPos)
        
        newPos = currentPos + 3
        # print(newPos)

        trackTurtle.insert(newPos, "T")

    #20% chance
    elif move >= 6 and move <= 7:

        trackTurtle.pop(currentPos)
        
        newPos = currentPos - 6
        if newPos < 0:
            newPos = 1

        # print(newPos)

        trackTurtle.insert(newPos, "T")

    #30% chance
    elif move >= 8 and move <= 10:

        trackTurtle.pop(currentPos)
        
        newPos = currentPos + 1
        # print(newPos)

        trackTurtle.insert(newPos, "T")

def HareMove():

    move = random.randint(1, 10)
    # print(f"è uscito: {move}")

    currentPos = trackHare.index("H")

    if move >= 1 and move <= 2:
        pass

    elif move >= 3 and move <= 4:

        trackHare.pop(currentPos)
        
        newPos = currentPos + 9

        trackHare.insert(newPos, "H")

    elif move == 5:

        trackHare.pop(currentPos)
        
        newPos = currentPos - 12
        if newPos < 0:
            newPos = 1

        trackHare.insert(newPos, "H")

    elif move >= 6 and move <= 8:

        trackHare.pop(currentPos)
        
        newPos = currentPos + 1

        trackHare.insert(newPos, "H")

    elif move >= 9 and move <= 10:

        trackHare.pop(currentPos)
        
        newPos = currentPos - 2
        if newPos < 0:
            newPos = 1

        trackHare.insert(newPos, "H")

        
def Position():
    print(f"La tartaruga si trova alla posizione: {trackTurtle.index('T')}")
    print(f"La lepre si trova alla posizione: {trackHare.index('H')}\n")
    print("\n")



print("BANG !!!! AND THEY'RE OFF !!!!!\n")

#Starting the loop
while True:
    
    TurtleMove()
    HareMove()
    Position()
    
    time.sleep(0.25)

    print(*trackTurtle)
    print("\n")
    print(*trackHare)
    print("\n")

    if trackTurtle.index("T") > 1 and trackHare.index("H") > 1:
        if trackTurtle.index("T") == trackHare.index("H"):
            print("OUCH!\n")

    if trackTurtle.index("T") == 70:
        print("Turtle wins!")
        break
    elif trackHare.index("H") == 70:
        print("Hare wins")
        break

