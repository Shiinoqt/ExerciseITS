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
    case (x, y) if x > 0 and y > 0:
        print(f"Il punto {coords} si trova nel primo quadrante.")
    case (x, y) if x < 0 and y > 0:
        print(f"Il punto {coords} si trova nel secondo quadrante.")
    case (x, y) if x < 0 and y < 0:
        print(f"Il punto {coords} si trova nel terzo quadrante.")
    case (x, y) if x > 0 and y < 0:
        print(f"Il punto {coords} si trova nel quarto quadrante.")
    
