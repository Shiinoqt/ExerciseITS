def verify(x, y, z) -> None:

    if x and (y or z):
        return print("Azione permessa")
    
    else:
        return print("Azione negata")