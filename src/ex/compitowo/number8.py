from collections import Counter #Im using this function to count how many times a number appears in the list

def count_isolated(numbers: list[int]) -> int:

    count_isolated = 0 #Here I save the count of isolated numbers

    number_counts = Counter(numbers) #Using the Counter function
    
    #For each number it iterates I check if the number appears only once in the list 
    for number in number_counts:

        if number_counts[number] == 1: #Here's the check
            
            count_isolated += 1 #I update the count of isolated numbers
    
    return count_isolated


print(count_isolated([1, 2, 3, 4, 5]))  # Output: 5 (all numbers are isolated)
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))  # Output: 2 (1 and 4 are isolated)


# Example usage
# print(count_isolated([1, 2, 3, 4, 5]))  # Output: 5 (all numbers are isolated)
# print(count_isolated([1, 2, 2, 3, 3, 3, 4]))  # Output: 2 (1 and 4 are isolated)