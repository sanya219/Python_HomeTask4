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

Task3()


