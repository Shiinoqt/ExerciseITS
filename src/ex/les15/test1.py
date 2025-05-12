with open("example2.txt", mode="w", encoding="utf-8") as file:
    
    message : str = "brr brr patapim"
    written_char : int = file.write(message)
    print(f"Written {written_char} characters to the file.")