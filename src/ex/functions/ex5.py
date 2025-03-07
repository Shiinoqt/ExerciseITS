def add_one(a: int) -> int:
    return a + 1

def add_one_to_list(mylist: list) -> list:
    
    new_list: list = []
    
    for number in mylist:
        new_list.append(add_one(number))
    
    print(new_list)

add_one_to_list([1, 2, 3])    
