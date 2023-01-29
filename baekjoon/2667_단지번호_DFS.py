# https://www.acmicpc.net/problem/2667
# DFS

N = int(input())
result = []
arr = [list(map(int, list(input()))) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    global cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 1:
            cnt += 1
            arr[nx][ny] = 0
            DFS(nx, ny)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[i][j] = 0
            cnt = 1
            DFS(i, j)
            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)