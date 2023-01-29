def permutation(now, end):
    if now == end:
        result.append(picked.copy())
        return
    for i in range(len(data)):
        if visited[i] == False:
            visited[i] = True
            picked[now] = data[i]
            permutation(now+1, end)
            visited[i] = False

N, M = 5, 3
data = range(1, N+1)
visited = [False] * N
picked = [False] * M
result = []

permutation(0, M)
for r in result:
    print(r)
print(len(result))