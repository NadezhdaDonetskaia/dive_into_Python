from typing import Generator
import os
# ✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def get_prime_numbers(n: int) -> Generator:
    count = 0
    current_number = 2
    while count < n:
        if is_prime(current_number):
            yield current_number
            count += 1
        current_number += 1


prime_n = get_prime_numbers(5)
print(next(prime_n))
print(next(prime_n))
print(next(prime_n))
print(next(prime_n))
print(next(prime_n))
try:
    print(next(prime_n))
except StopIteration:
    print('Генератор закончился')
else:
    print('Что-то пошло не так')


# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def split_path(file_path: str) -> tuple[str, str, str]:
    directory, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return directory, name, extension


current_file_path = os.path.abspath(__file__)
print(split_path(current_file_path))

# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

names = ["Alice", "Bob", "Charlie"]
rates = [1000, 1500, 2000]
bonuses = ["10.25%", "5.5%", "7.75%"]

result_dict = {name: rate * (1 + float(bonus.strip('%')) / 100)
               for name, rate, bonus in zip(names, rates, bonuses)}

print(result_dict)


# ✔ Создайте функцию генератор чисел Фибоначчи.

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci_generator()

for i in range(1, 11):
    print(f'Число Фибоначи №{i}: {next(gen)}')
