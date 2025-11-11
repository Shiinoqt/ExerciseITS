import string
def counter_words (lista: list[str]) -> dict[str, int]:
    wordDict : dict[str, int] = {}
    listnopunct = []

    for word in lista:
        word = word.lower()
        for char in string.punctuation:
            word = word.replace(char, "")
        listnopunct.append(word.split())

    print(listnopunct)
    for words in listnopunct:
        for w in words:
            if w not in wordDict:
                wordDict[w] = 1
            else:
                wordDict[w] += 1

    return wordDict

text = ["Hello, world!", "Hello... PYTHON?", "world.","exciting world of Python."]

def sorting (lista: list[int]) -> list[int]:
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista




sorted_list = sorting([5,3,8,6,2,7,4,1])
print(sorted_list)

def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    result: dict[str, list[int]] = {}
    for key, value in tuples:
        if key not in result:
            result[key] = []
        result[key].append(value)

def merge_dicts(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    merged: dict[str, int] = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

def trova_chiave_per_valore(dizionario: dict[str, int], valore: int) -> list[str]:
    chiavi: list[str] = []
    for key, val in dizionario.items():
        if val == valore:
            chiavi.append(key)
    return chiavi

a = {"x": 1, "y": 2}
b = {"a": 3}






merged = a | b
a |= b

for key, value in a.items():
    print(key, value)
