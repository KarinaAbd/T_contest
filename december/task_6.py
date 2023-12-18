# Поздравляю, вы дошли до серьёзной задачи, больше никаких легенд, только хардкор.
# Дан массив a из n целых чисел. Требуется выполнить q запросов такого вида (1 ≤ l ≤ r ≤ n, 0 ≤ k, b, x ≤ 10 ):
# + l r x — прибавить x ко всем ai на отрезке i ∈ [l, r]
# ? l r k b — вывести maxl≤i≤r min(ai , k ⋅ i + b)

# Формат входных данных
# В первой строке заданы два числа n, q(1 ≤n≤2⋅10^5 , 1 ≤ q ≤ 5 ⋅ 10^5 ).
# Во второй строке задан массив a (0 ≤ ai ≤ 10^9).
# ​Следующие q строк содержат запросы в заданном формате. Гарантируется, что будет хотя бы один запрос типа ?.

# Формат выходных данных
# Для каждого запроса типа ? выведите ответ в отдельной строке.

# Примеры данных
# Ввод
# 6 3
# 2 4 6 8 10 12
# ? 2 5 3 0
# + 2 3 6
# ? 2 5 3 2

# Вывод
# 10
# 11

_, q = map(int, input().split())
nums = [-1]
nums.extend(list(map(int, input().split())))

result = []

for _ in range(q):
    question = list(input().split())

    if len(question) == 4:
        id = int(question[1])
        id_r = int(question[2])
        x = int(question[3])

        while id <= id_r:
            nums[id] += x
            id += 1

    elif len(question) == 5:
        id_l = int(question[1])
        id_r = int(question[2])
        k = int(question[3])
        b = int(question[4])

        res = [min(num, k * i + b) for i, num in enumerate(nums) if i in range(id_l, id_r + 1)]
   
        result.append(max(res))

for r in result:
    print(r)
