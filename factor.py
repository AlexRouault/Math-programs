def factor(n):
    factors = []
    square_root = int(n ** (1/2))
    for pf in range(1, square_root + 1):
        if n % pf == 0:
            factors.append(pf)
    index = len(factors)-1
    if factors[index] == square_root:
        index -= 1
    while index >= 0:
        factors.append(n // factors[index])
        index -= 1
    return factors

            
print(factor(100324103481))
