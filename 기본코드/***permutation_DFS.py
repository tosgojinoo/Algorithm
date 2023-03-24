# 5개 숫자 중 3개 순열
# backtracking
def permutation(depth):
    if depth == R:
        result.append(picked[:])
        return
    for i in range(len(arr)):
        if visited[i] == False:
            visited[i] = True
            picked[depth] = arr[i]
            permutation(depth+1)
            visited[i] = False

N, R = 5, 3
arr = range(1, N+1)
visited = [False] * N
picked = [False] * R
result = []

permutation(0)
print(result)
print(len(result))