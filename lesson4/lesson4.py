from typing import Any
# Напишите функцию для транспонирования матрицы


def matrix_transpose(matrix: list[list]) -> list[list]:
    transposed_matrix = [
        [row[i] for row in matrix]
        for i in range(len(matrix[0]))]
    return transposed_matrix


# print(matrix_transpose(
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9],
#     ]
# ))

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def create_arg_dict(**kwargs: Any) -> dict:
    arg_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, float, str, bool, tuple)):
            arg_dict[value] = key
        else:
            arg_dict[str(value)] = key
    return arg_dict


# print(create_arg_dict(
#     a=10,
#     b=3.14,
#     c="hello",
#     d=True,
#     e=[1, 2, 3],
#     f=(1, 2, 3)))
# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# текст в файле ATM


account = [0, ]


def get_balance(acc=account):
    return sum(account)


def charge_interest(acc=account,
                    multiplicity=3,
                    persent=3):
    if len(acc) % multiplicity == 0:
        return get_balance() * persent // 100
    return 0


def top_up(val, acc=account):
    acc.append(val)
    proc = charge_interest()
    acc[-1] += proc
    return get_balance()


def pull_off(val, acc=account, multiplicity=50):
    if val % multiplicity != 0:
        print(f'Значение не кратно {multiplicity}')
        return get_balance()
    if account[-1] - val < 0:
        print('Значение больше остатка')
        return get_balance()
    acc.append(-val)
    proc = charge_interest()
    acc[-1] += proc
    return get_balance()


def exit():
    pass


print(get_balance())
print(pull_off(20))
print(pull_off(50))
print(top_up(50))
print(pull_off(50))
print(top_up(170))
print(get_balance())
print(account)
