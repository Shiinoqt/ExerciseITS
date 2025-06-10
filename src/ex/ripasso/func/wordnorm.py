import re

def uniqueWords (text: str) -> dict[str, int]:

    wordDict: dict[str, int] = {}
    #wordsStrip = ""
    
    #for words in text:
    #    x = words.strip(",.!?").lower()
    #    wordsStrip += x

    words = re.findall(r'\w+', text.lower())

    for word in words:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1
    
    return wordDict

text = "Hello, world! Hello... PYTHON? world."
output = print(uniqueWords(text))