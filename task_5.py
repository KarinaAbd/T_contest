# Во время разработки некоторой задачи Саша решил сгенерировать несколько новых тестов.
# Каждый тест Саши должен представлять собой натуральное число, не меньшее l и не большее r.
# Кроме того, натуральное число в тесте обязательно должно состоять из одинаковых цифр.
# Например, число 999 подходит под это требование, а число 123 — нет.
# Какое максимальное число различных тестов сможет создать Саша?

# Формат входных данных 
# В единственной строке вводятся два натуральных числа l,r (1≤l,r≤10^18) — ограничения на тесты Саши.
# Обратите внимания, что эти числа не вместятся в 32-битный тип данных, используйте 64-битный при необходимости

# Формат выходных данных
# Выведите одно число — количество тестов, которое может сделать Саша.

# Замечание
# В первом тесте Саше подходят номера [4,5,6,7].
# Во втором тесте подходят все числа, кратные 11, от 11 до 99.


def generate_test(minimum, maximum):
    if maximum < 10:
        return maximum - minimum + 1
    number = 1    
    tests = []
    while True:
        if number == maximum:
            break
        if number >= minimum and number < 10:
            tests.append(number)

        new = number * 10 + number
        if new >= minimum and new <= maximum:
            tests.append(new)
        number += 1
    return len(tests)


assert generate_test(4, 7) == 4
assert generate_test(10, 100) == 9
assert generate_test(1, 20) == 10
assert generate_test(11, 20) == 1
assert generate_test(12, 20) == 0
assert generate_test(11, 22) == 2
