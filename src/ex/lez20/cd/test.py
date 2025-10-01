# Chapter 1
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


# Chapter 2
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



def deep_get(d: dict | list, path: list, default=None):
    current = d
    for key in path:
        if isinstance(current, dict):
            current = current.get(key, default)
        elif isinstance(current, list) and isinstance(key, int):
            if 0 <= key < len(current):
                current = current[key]
            else:
                return default
        else:
            return default
    return current

# Chapter 3
def unique_count(nums: list) -> int:
    return len(set(nums))

def intersection_sorted(a: list[int], b: list[int]) -> list[int]:
    res = []
    seen = set()
    
    for n in a:
        if n in b and n not in seen:
            res.append(n)
            seen.add(n)
    
    return res

def symdiff_sorted(a: list[int], b: list[int]) -> list[int]:
    result = []
    
    # Elements in a but not in b
    for n in a:
        if n not in b:
            result.append(n)
    
    # Elements in b but not in a
    for n in b:
        if n not in a:
            result.append(n)
    
    return sorted(list(set(result)))  # Remove duplicates and sort


def are_anagrams(a: str, b: str) -> bool:
    # Remove all spaces and convert to lowercase
    a1 = a.lower().replace(' ', '')
    b1 = b.lower().replace(' ', '')
    
    # Check if sorted characters are equal
    return sorted(a1) == sorted(b1)


def powerset_size(n: int) -> int:
    return 2 ** n

# Chapter 4
def add(x, y):
    return x + y