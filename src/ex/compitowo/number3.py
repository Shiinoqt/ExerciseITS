def remove_duplicates(urlist: list) -> list:
    
    #I create a new list to store the unique elements
    noDuplicates = []
    
    for i in urlist:

        #If the element is not in the noDuplicates list I append it
        if i not in noDuplicates:
            noDuplicates.append(i)
    
    return noDuplicates
