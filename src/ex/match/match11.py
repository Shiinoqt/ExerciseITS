x = int(input("type x: "))
y = int(input("type y: "))

coords : tuple[int, int]= (x, y)

match coords:
    case (0,0):
        print(f"Il punto {coords} si trova nell'origine.")
    case (x, 0):
        print(f"Il punto {coords} si trova sull'asse X.")
    case (0, y):
        print(f"Il punto {coords} si trova sull'asse Y.")
    case a if x > 0 and y > 0:
        print(f"Il punto {coords} si trova nel primo quadrante.")
    case b if x < 0 and y > 0:
        print(f"Il punto {coords} si trova nel secondo quadrante.")
    case c if x < 0 and y < 0:
        print(f"Il punto {coords} si trova nel terzo quadrante.")
    case d if x > 0 and y < 0:
        print(f"Il punto {coords} si trova nel quarto quadrante.")
    
