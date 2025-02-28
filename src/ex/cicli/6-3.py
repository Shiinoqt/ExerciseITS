glossary : dict[str]= {"int": "Integer", "str": "String", "bool": "Boolean", "list": "A list", "dict": "A dictionary"}

for elem in glossary:
    print(f"\n{elem.title()} is an {glossary[elem].lower()}")
