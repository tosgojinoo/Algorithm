# 중복 순열
def permutation_repetition(now, end):
    global picked
    if now == end :
        result.append(str(int(''.join(picked))))
        return
    else:
        for i in range(len(data)):
            picked[now] = str(data[i])
            permutation_repetition(now+1, end)


data = [0, 1, 2, 3, 4, 7]
N, M = len(data), 3
picked = [False] * M
result = []

permutation_repetition(0, 3)