# 2. Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def get_hex(n: int) -> hex:
    hex_chars = '0123456789abcdef'
    if n == 0:
        return "0"
    hex_string = ""
    while n > 0:
        remainder = n % 16
        hex_string = hex_chars[remainder] + hex_string
        n //= 16
    return hex_string


print(hex(10)[2:]==get_hex(10))
print(hex(35)[2:]==get_hex(35))
print(hex(15896)[2:]==get_hex(15896))
# 3. Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def get_num_den(fraction: str) -> tuple[int, int]:
    return list(map(int, fraction.split('/')))


def sum_fractions(fraction1: str, fraction2: str) -> str:
    num1, den1 = get_num_den(fraction1)
    num2, den2 = get_num_den(fraction2)
    common_denominator = den1 * den2
    num1 *= den2
    num2 *= den1
    result_num = num1 + num2
    greatest_common_divisor = gcd(result_num, common_denominator)
    result_num //= greatest_common_divisor
    common_denominator //= greatest_common_divisor
    return '/'.join(map(str, [result_num, common_denominator]))


def mult_fractions(fraction1: str, fraction2: str) -> str:
    num1, den1 = get_num_den(fraction1)
    num2, den2 = get_num_den(fraction2)
    result_num = num1 * num2
    result_den = den1 * den2
    greatest_common_divisor = gcd(result_num, result_den)
    result_num //= greatest_common_divisor
    result_den //= greatest_common_divisor
    return '/'.join(map(str, [result_num, result_den]))


def sum_and_mult_fractions(
        fraction1: str, fraction2: str) -> tuple[str, str]:
    sum_ = sum_fractions(fraction1, fraction2)
    mult_ = mult_fractions(fraction1, fraction2)
    return sum_, mult_


print(sum_and_mult_fractions('1/2', '3/4'))


from fractions import Fraction

# Создаем объекты Fraction
fraction_1 = Fraction(1, 2)
fraction_2 = Fraction(3, 4)

# Вычисляем сумму и произведение дробей
sum_result = fraction_1 + fraction_2
product_result = fraction_1 * fraction_2

print(sum_result)
print(product_result)