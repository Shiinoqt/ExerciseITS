def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if item == element:
            return True
    return False


# def find_element(lst: list[int], element: int) -> bool:
    
#     #Here I save the answer
#     answer = None

#     for item in lst:
        
#         if item == element:
#             answer = True
#             break #I stop the loop when I get True and return the answer
        
#         else:
#             answer = False
            
#     return answer
    

# def find_element(lst: list[int], element: int) -> bool:
#     for item in lst:
#         if item == element:
#             return True
#     for item in lst:
#         if item != element:
#             return False
    
print(find_element([1, 5, 3, 4, 2], 5))
print(find_element([1, 2, 3, 4, 5], 6))
print(find_element([10, 20, 30], 20))