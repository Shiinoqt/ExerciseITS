def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    # Funzione per la somma degli elementi di due liste con il check della lunghezza
    if len(x) == len(y):
        for i in range(len(x)):
            x[i] = x[i] + y[i]
    
    else:
        print("Le liste non hanno la stessa lunghezza")  
    
    return x
  

print(somma_elementi([1, 2, 3, 4], [4, 5, 6]))
