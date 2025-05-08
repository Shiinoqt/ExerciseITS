PATH: str = "Exercise/src/ex/les15/example.txt"
mode: str = "r"  # "r" Read mode "w" Write mode "a" Append mode
# "r+" Read and write mode "w+" Write and read mode
# "a+" Append and read mode
encoding: str = "utf-8"  # Encoding type

# Example usage
file = open(PATH, mode, encoding=encoding)
output = file.read()  # Read the entire file
print(output)
file.close()