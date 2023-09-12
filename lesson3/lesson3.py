from collections import Counter
import os
import re
from itertools import combinations

# 1) Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


def get_doubles(coll: list) -> list:
    count_el = Counter(coll)
    return [el for el, count in count_el.items() if count > 1]


# print(get_doubles([1, 1, 1, 2, 3, 3, 4, 5, 5, 5]) == [1, 3, 5])

# 2) В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.


def common_word(text: str) -> list[str]:
    words = re.findall(r'\b\w+\b', text.lower())
    most_common_words = Counter(words).most_common(10)
    return [word for word, count in most_common_words]


current_dir = os.path.dirname(os.path.abspath(__file__))
txt_file_path = os.path.join(current_dir, "text.txt")
with open(txt_file_path) as t:
    text = t.read()

# print(common_word(text))


# 3) Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


def knapsack(items: dict[str: int], max_weight: int) -> list[str]:
    # если нам нужен один вариант:
    # weight_things = list(items.values())
    # things = list(items.keys())
    # if sum(weight_things) <= max_weight:
    #     return weight_things

    res = list(items.items())
    n = len(res) - 1
    result = []
    while n > 0:
        comb = list(combinations(res, n))
        for el in comb:
            if sum([w for _, w in el]) <= max_weight:
                # если нам нужен только первый вариант:
                # return[t for t, _ in el]
                result.append([t for t, _ in el])
        n -= 1
    return result


th = {
    "Книга": 1,
    "Бутерброды": 2,
    "Вода": 4,
    "Термос": 3,
}

# print(knapsack(th, 3))


# Задание №8
# Погружение в Python | Коллекции
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:

# ✔ Какие вещи взяли все три друга


# ✔ Какие вещи уникальны, есть только у одного друга

# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует


# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.


friends_items = {
    "Друг1": {"тент", "спальник", "фонарик", "палатка"},
    "Друг2": {"спальник", "фонарик", "гитара", "еда"},
    "Друг3": {"тент", "фонарик", "еда", "сапоги"}
}


def get_all_items(friends_items: dict) -> set:
    return set.union(*friends_items.values())


def get_unic_items(friends_items: dict) -> set:
    unique_items = set()

    for friend, items in friends_items.items():
        other_friends_items = set.union(*(
            friends_items[f] for f in friends_items if f != friend))
        unique_items.update(items.difference(other_friends_items))
    return unique_items


def find_items_common_except_one(friends_items: dict) -> tuple[set, str]:
    res_items = get_all_items(friends_items)
    res_name = ''
    for item in res_items.copy():
        count = 0
        name = ''
        for friend, items in friends_items.items():
            if item in items:
                count += 1
            else:
                name = friend
        if count == len(friends_items) - 1:
            res_name = name
        else:
            res_items.remove(item)
    return res_items, res_name


print(get_all_items(friends_items))
print(get_unic_items(friends_items))
print(find_items_common_except_one(friends_items))
