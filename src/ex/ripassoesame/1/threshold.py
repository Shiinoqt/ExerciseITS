def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    result = 0
    for n in numbers:
        if n > threshold:
            result += n

    return result