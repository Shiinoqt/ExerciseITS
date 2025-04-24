def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0

    while rimbalzi < 5:
        
        if altezza < 0:
            print(f"Tempo: {tempo} Rimbalzo!")
            altezza *= -0.5
            velocita *= -0.5
            rimbalzi += 1
            
        else:
            print(f"Tempo: {tempo} Altezza: {altezza}")
            altezza += velocita
            velocita -= 96

        tempo += 1

