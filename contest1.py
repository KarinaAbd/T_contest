n, s = map(int, input().split()) # кол-во револьверов и долларов
prices = list(map(int, input().split())) # цены n ревеольверов
result = 0
for i in range(n):
    curr_price = prices[i]
    if curr_price < s and curr_price > result:
        result = curr_price

print(result)
