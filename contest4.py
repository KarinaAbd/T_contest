n, m = map(int, input().split())
money_type = list(map(int, input().split()))

money = money_type * 2
money.sort()
res = []
new_money = []
flag = 1

while money:
    res.append(money.pop())
    if sum(res) == n:
        print(len(res))
        res.sort()
        print(' '.join(list(map(str, res))))
        flag = 0
        break
    elif sum(res) < n:
        continue
    elif sum(res) > n:
        new_money.append(res.pop())
    if len(money) == 0 and new_money:
        money = new_money
        money.sort()
        new_money = []
        res.pop(0)

if flag:
    print(-1)
