from collections import Counter

letters = input()
cnt = Counter(letters)
res = 0

for l in 'sherif':
    if l != 'f' and cnt[l] > 0:
        if res == 0 or res > cnt[l]:
            res = cnt[l]
    elif l == 'f' and cnt[l] > 0:
        cnt_f = cnt[l] // 2
        res = cnt_f if res > cnt_f else res
    elif cnt[l] == 0:
        res = 0
        break

print(res)
