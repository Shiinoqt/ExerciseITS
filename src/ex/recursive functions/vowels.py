def vowelsCounter(string: str) -> int:

    if string == "":
        return 0
    
    else:
        if string[0].lower() in "aeiou":
            return 1 + vowelsCounter(string[1:])
        else:
            return 0 +  vowelsCounter(string[1:])
        

      
print(vowelsCounter("Hello World"))