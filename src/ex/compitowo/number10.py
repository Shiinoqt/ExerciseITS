def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    
    #Copy of the first dictionary to not change original values
    newDict = dict1.copy()
    
    #Iterating to add to the new dictionary elements of the second dictionary
    for key, value in dict2.items():
        newDict[key] = value
        
        #Checking if the iterating keys are in the first dictionary then I sum them and add them to the new dictionary
        if key in dict1:
            newDict[key] = dict1[key] + dict2[key]

    return newDict