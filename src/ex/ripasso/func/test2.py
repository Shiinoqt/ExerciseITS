def multiply(numbers: list[int], threshold: int) -> int:

    start = 1

    for number in numbers:

        if number < threshold:
            start = number * start

    return start

