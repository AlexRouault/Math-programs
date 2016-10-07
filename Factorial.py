def factorial (factorialee):
    fact_so_far=1
    fact_multiplier=1
    while fact_multiplier<=factorialee:
        fact_so_far*=fact_multiplier
        fact_multiplier+=1
    return fact_so_far
print(factorial(3000))

