# ex. 10
age = int(input("Type your age: "))
if age >= 18 and age <= 65:
    print("Allowed to participate")
elif age < 18:
    print("Not allowed you're a minor.")
else:
    print("Not allowed over max age.")