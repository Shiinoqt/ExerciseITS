tutor = 10
waiting = 0
while waiting < 50:
    student = (input("Name student: "))
    if tutor > 0:
        print("Tutor assigned")
        tutor = tutor - 1
    else:
        waiting += 1
        print(f"Added to the waiting list. {waiting}")
print("Waiting list full.")

