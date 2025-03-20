def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    
    #Simple check of conditions
    if conditionA == True or (conditionB == True and conditionC == True):
        return "Operazione permessa"
    
    else:
        return "Operazione negata"