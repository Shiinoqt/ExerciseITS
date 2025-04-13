def prime_factors(n: int) -> list[int]:

    #List to store prime factors
    factors = []

    #Starting with the smallest prime factor
    i = 2

    while n >= 2:
        
        #Check if i is a factor of n then add it to the list of factors
        if n % i == 0:
            factors.append(i)

            #Divide n by i to reduce it
            n = n // i

        else:
            i += 1

    return factors