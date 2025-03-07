# ex. 3
status = True

while status:
    nameCourse = str(input("Type course name: "))
    max = 100
    while True:
        option = str(input("Select option: "))
        if option.lower() == "add":
            if max > 0:
                max -= 1
            else:
                print("No available seat")
        elif option.lower() == "remove":
            if max < 100:
                max += 1
            else: 
                print("Seats already available")
        elif option.lower() == "show":
            print(f"Free seats: {max}, Occupied seats: {100 - max}")
        elif option.lower() == "delete":
            break
        elif option.lower() == "quit":
            status = False
            break