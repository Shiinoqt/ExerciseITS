import json

PATH: str = "Exercise/src/ex/les15/config.json"
mode: str = "r"
encoding: str = "utf-8"

with open(PATH, mode=mode, encoding=encoding) as file:

    # Read the JSON data from the file
    config: dict = json.load(file)


# Add a new key-value pair to the dictionary
config['newSetting'] = "newValue" 

with open(PATH, mode= "w") as file:

    # Write the updated JSON data back to the file
    json.dump(config, file, indent=4)



# # Print the data
# print(f"appName: {config['appName']}, version: {config['version']}")


