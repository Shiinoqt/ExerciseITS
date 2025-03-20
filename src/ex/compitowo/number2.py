def rotate_left(elements: list, k: int) -> list:
    
    #I slice the list using the range till the end and backwards and sum it
    elements = elements[k:] + elements[:k]
    
    #If we encounter a k longer than the elements of the list  
    if k > len(elements):
        k = k - len(elements)
        elements = elements[k:] + elements[:k]

    return elements


# def rotate_left(elements: list, k: int) -> list:

#     elementsSliced = elements[k:] + elements[:k]

#     return elementsSliced


print(rotate_left([1, 2, 3, 4, 5], 2))
print(rotate_left([1, 2, 3, 4, 5], 3))
print(rotate_left([1, 2, 3, 4, 5], 4))