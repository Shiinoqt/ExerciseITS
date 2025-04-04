def find_disappeared_numbers(nums: list[int]) -> list[int]:
    
    # Store the disappeared numbers
    disappeardedNumbers = []

    # Creating a list of numbers from 1 to n
    numbersList = range(1, len(nums) + 1)

    # Comparing each numbers between the two lists
    for i in range(len(nums)):

        if numbersList[i] not in nums:
            disappeardedNumbers.append(numbersList[i])

    return disappeardedNumbers

# Test cases
print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5, 6]
