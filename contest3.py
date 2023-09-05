n = int(input())
curr_numbers = list(map(int, input().split()))
target_numbers = list(map(int, input().split()))
result = 'YES'

if n >= 2:
    res = []
    for i in range(n):
        if curr_numbers[i] != target_numbers[i]:
            res.append(i)
    if res:
        sorted_part = sorted(curr_numbers[res[0]:res[-1] + 1])
        temp = curr_numbers[:res[0]] + sorted_part + curr_numbers[res[-1] + 1:]
        if target_numbers != temp:
            result = 'NO'

print(result)
