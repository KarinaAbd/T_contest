n, m = map(int, input().split())
questions = []
for _ in range(m):
    question = tuple(map(int, input().split()))
    questions.append(question)

bands = [[num] for num in range(1, n + 1)]
ghost_info = {num: 1 for num in range(1, n + 1)}

for question in questions:
    if question[0] == 1:
        _, x, y = question
        ind_x = 0
        ind_y = 0
        for i in range(n):
            if x in bands[i]:
                ind_x = i
            if y in bands[i]:
                ind_y = i
        if ind_x == ind_y:
            continue
        bands[ind_x].extend(bands[ind_y])
        bands[ind_y] = []
        for ghost in bands[ind_x]:
            ghost_info[ghost] += 1

    elif question[0] == 2:
        _, x, y = question
        result = 'NO'
        for band in bands:
            if x in band and y in band:
                result = 'YES'
        print(result)

    elif question[0] == 3:
        _, x = question
        print(ghost_info[x])
