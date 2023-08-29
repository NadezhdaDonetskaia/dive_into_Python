# 1.Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
def multiplication_table(start=2, finish=9):
    results = ''
    for x in range(start, finish+1):
        res = []
        for y in range(start, finish+1):
            res.append(x * y)
        results += ' '.join([f'{x}'
                             if len(f'{x}') > 1 else f' {x}'
                             for x in res])
        results += '\n'

    results = results[:-1]
    return results


# print(multiplication_table())


# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def triangle(a, b, c):
    sides = sorted([a, b, c])
    if not sides[0] + sides[1] > sides[2]:
        return 'triangle not exist'
    if a == b and b == c:
        return 'triangle is equilateral'
    if a == b or b == c:
        return 'triangle is isosceles'
    return 'triangle is versatile'


# print(triangle(2, 3, 4))

# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_simple_number(num):
    if num <= 0 or num > 100000:
        return 'Please enter a positive number up to 100,000'
    index = 0
    for x in range(2, num + 1):
        if num % x == 0:
            index += 1
        if index > 2:
            return 'Number is not simple'
    return 'Number is simple'


# print(is_simple_number(8))


# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:

# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint


def compare_numbers(base_n, answer_n):
    if base_n > answer_n:
        print('Загаданное число больше!')
    else:
        print("Загаданное число меньше!")


def guess_number(n=1000):
    number = randint(0, n)
    print(f'Я загадал какое-то число до {n}\nПопробуй его угадать!')
    for i in range(10, 0, -1):
        print(f'Осталось {i} попыток')
        answer = int(input('Введи число: '))
        if number == answer:
            return 'Поздравляю, вы угадали число!'
        compare_numbers(number, answer)
    return f'Попытки кончились =(\nЧисло было {number}'


print(guess_number())
