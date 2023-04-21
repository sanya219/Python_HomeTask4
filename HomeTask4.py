import math

# Задача 1. Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.
# 60 -> 2, 2, 3, 5
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

def Task1():
    print("Задача 1")
    N = int(input("Введите число: "))
    factors, count = prime_factors(N)
    print(f"Простые множители числа {N}: {factors}")
    print(f"Количество простых множителей: {count}")

#Task1()

# Задача 2. В первом списке находится информация об ассортименте мороженного, во втором списке - информация о том, 
# какое мороженное есть на складе. Выведите названия того товара, который закончился.
# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»

def Task2():
    print("\nЗадача 2:")
    assortment = ["Сливочное", "Бурёнка", "Вафелька", "Сладкоежка"]
    stock = ["Сливочное", "Вафелька", "Сладкоежка"]

    assortment_set = set(assortment)
    stock_set = set(stock)
    out_of_stock = assortment_set - stock_set
    print("Закончилось:", ", ".join(f'«{item}»' for item in out_of_stock))

#Task2()

# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.

def Task3():
    print("\nЗадача 3:")
    precision = float(input("Введите толчность в виде десятичной дроби: "))
    signs = 0
    while precision < 1:
        precision *= 10
        signs +=1
    print(f"Число ПИ с точностью: {signs} знаков: {round(math.pi, signs)}")

#Task3()

# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 2. 3x^2 + x + 8
# 3. Результат: 8x^2 + 4x + 8
# Запишем многочлены в файлы

def parse_polynomial(poly_str):
    terms = poly_str.split(' + ')
    parsed_poly = {}
    
    for term in terms:
        if 'x^' in term:
            coef, _, power = term.partition('x^')
            coef = int(coef) if coef else 1
            parsed_poly[int(power)] = int(coef)
        elif 'x' in term:
            coef, _, _ = term.partition('x')
            coef = int(coef) if coef else 1
            parsed_poly[1] = coef
        else:
            parsed_poly[0] = int(term)
    
    return parsed_poly

def add_polynomials(poly1, poly2):
    result = poly1.copy()
    
    for power, coef in poly2.items():
        if power in result:
            result[power] += coef
        else:
            result[power] = coef
            
    return result

def Task4():
    with open("polynomial1.txt", "r") as file1:
        poly1_str = file1.read()
        poly1 = parse_polynomial(poly1_str)

    with open("polynomial2.txt", "r") as file2:
        poly2_str = file2.read()
        poly2 = parse_polynomial(poly2_str)

    result_poly = add_polynomials(poly1, poly2)

    result_str = " + ".join(f"{coef}x^{power}" if power > 1 else (f"{coef}x" if power == 1 else str(coef)) for power, coef in sorted(result_poly.items(), reverse=True))
    print(f"Результат: {result_str}")

Task4()

