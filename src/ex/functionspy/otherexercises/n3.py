# def prime_factors(n: int) -> list[int]:

#     factors = []
#     i = 2

#     while n >= 2:
#         if n % i == 0:
#             factors.append(i)
#             n = n / i
#         else:
#             i += 1

#     return factors

def prime_factors(n):

    factors = []
    i = 2    
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    
    if n > 1:
        factors.append(n)
    
    return factors



print(prime_factors(4))
print(prime_factors(60))