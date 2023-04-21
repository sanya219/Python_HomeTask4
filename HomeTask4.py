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
    return factors, len(factors)

# Пример использования
N = 315
factors, count = prime_factors(N)
print(f"Простые множители числа {N}: {factors}")
print(f"Количество простых множителей: {count}")
