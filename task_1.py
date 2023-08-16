# 1 Задача Мобайл

# Костя подключен к мобильному оператору «Мобайл». Абонентская плата Кости составляет А рублей в месяц. 
# За эту стоимость Костя получает B мегабайт интернет-трафика. 
# Если Костя выйдет за лимит трафика, то каждый следующий мегабайт будет стоить ему C рублей.
# Костя планирует потратить D мегабайт интернет-трафика в следующий месяц. 
# Помогите ему сосчитать, во сколько рублей ему обойдется интернет.

# Формат входных данных
# Вводится 4 целых положительных числа A,B,C,D(1≤A,B,C,D≤100) — стоимость тарифа Кости, размер тарифа Кости,
# стоимость каждого лишнего мегабайта, размер интернет-трафика Кости в следующем месяце. 
# Числа во входном файле разделены пробелами.

# Формат выходных данных
# Выведите одно натуральное число — суммарные расходы Кости на интернет.


def calculate_payment():
    payment, plan_amount, extra_pay, real_amount = map(int, input().split())
    if real_amount > plan_amount:
        payment += (real_amount - plan_amount) * extra_pay
    print(payment)


calculate_payment()
