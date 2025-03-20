def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    
    for val in elements_to_remove:
        
        #We iterate and remove the value if it exists in the set (While using remove function gives error if not present)
        original_set.discard(val)

    return original_set