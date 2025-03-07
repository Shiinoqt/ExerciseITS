def check_each(mynumbers: list):
    for number in mynumbers:
        if number > 5:
            print(f"{number} is greater than 5")
        elif number < 5:
            print(f"{number} is less than 5")
        else:
            print(f"{number} is equal to 5")
    
check_each([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])