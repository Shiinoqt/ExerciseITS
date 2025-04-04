def even_odd_pattern(numbers:list[int]) -> list[int]:

    even = []
    odd = []

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even.append(numbers[i])
        else:
            odd.append(numbers[i])


    return even + odd





# Test cases
if __name__ == "__main__":
    # Test case 1
    numbers = [1, 2, 3, 4, 5]
    print(even_odd_pattern(numbers))  # Output: [2, 4, 1, 3, 5]

    # Test case 2
    numbers = [6, 7, 8, 9, 10]
    print(even_odd_pattern(numbers))  # Output: [6, 8, 10, 7, 9]

    # Test case 3
    numbers = [11, 12, 13]
    print(even_odd_pattern(numbers))  # Output: [12, 11, 13]