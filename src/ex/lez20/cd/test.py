def dedup_stable(nums: list[int]) -> list[int]:
    result: list = []
    lastSeen = None

    for n in nums:
        if n != lastSeen:
            result.append(n)

        lastSeen = n

    return result
        
print(dedup_stable([1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]))


def chunk(lst: list[int], size: int) -> list[list[int]]:
    slices: list[list[int]] = []
    for i in range(0, len(lst), size):
        slices.append(lst[i:i + size])
    return slices

print(chunk([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))


def letter_count(text: str) -> dict[str,int]:
    countL= {}
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

    for letter in text:
        if letter.isupper():
            continue
        elif letter in punctuation:
            continue
        elif letter in countL:
            countL[letter] += 1
        else:
            countL[letter] = 1

    return countL

print(letter_count("heLLLlo world!"))