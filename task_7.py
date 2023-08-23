# 7 Тайный Санта

# В школе перед Новым Годом устраивают игру в Тайного Санту.
# Каждому ученику i выдается ученик a от i, которому он сделает подарок.
# Костя, как администратор игры, определил каждому школьнику свое число a от i.
# Но потом его коллега Маша спросила: А правда ли, что если начать цепочку
# подарков от школьника 1 к школьнику a от 1, потом a от a от 1﻿ и так далее,
# то цепочка замкнется на школьнике 1, после того,
# как задействует всех остальных учеников ровно по одному разу?
# Костя не знает, правда это или нет, но собирается изменить одно число a от i,
# чтобы получить конфигурацию, которая устроит Машу. Помогите ему с этим.

# Формат входных данных
# В первой строке находится натуральное число n — количество школьников
#  (2≤n≤105). В следующей строке находится n натуральных чисел a от i — ученик,
#  который достался Тайному Санте с номером i(1≤a от i≤n).

# Формат выходных данных
# В первой строке выведите два числа (1≤x,y≤n,x≠y) — номер ученика x,
# которому нужно изменить число a от x, и новое значение a от x.
# Должно выполняться условие a от x ≠ y. Если ответов несколько — любой.
# Если сделать это невозможно — выведите −1 −1

# Примеры:
# Ввод:
# 3
# 1 2 3
# Вывод:
# -1 -1

# Ввод:
# 3
# 1 3 1
# Вывод:
# 1 2

def fix_gifts_list(quantity: int, gifts: list) -> tuple:
    gift_pairs = list(zip(range(1, quantity + 1), gifts))
    graph = {}
    no_gifts = []
    too_many = []

    for pair in gift_pairs:
        _, giftrecipient = pair
        graph[giftrecipient] = graph.get(giftrecipient, 0) + 1

    for num in range(1, quantity + 1):
        if num not in graph:
            no_gifts.append(num)

    for giftrecipient, count in graph.items():
        if count > 1:
            too_many.append(gifts.index(giftrecipient))

    if len(no_gifts) == 1 and len(too_many) == 1:
        gifts[too_many[0]] = no_gifts[0]

    for giftowner, giftrecipient in enumerate(gifts):
        if giftowner + 1 == giftrecipient:
            return -1, -1
    return too_many[0] + 1, no_gifts[0]


assert fix_gifts_list(3, [1, 2, 3]) == (-1, -1)
assert fix_gifts_list(3, [1, 3, 1]) == (1, 2)
assert fix_gifts_list(5, [1, 3, 1, 2, 5]) == (-1, -1)
assert fix_gifts_list(5, [1, 3, 1, 2, 4]) == (1, 5)
