def binary_search(list, x):
    low = 0 
    high = len(list) - 1 

    while low <= high: 
        mid = (low + high) // 2 
        guess = list[mid]

        if guess == x: 
            return mid
        if guess > x: 
            high = mid - 1
        else: 
            low = mid + 1
            
    return None 
