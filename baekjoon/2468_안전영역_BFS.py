from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
height_max = max(map(max, arr))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    global visited
    # deque: 양방향 큐
    q = deque([(x, y)])
    # q.append((x, y))

    while q:
        # Pop element from the start
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny]>height and visited[nx][ny]==0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

result = []
for height in range(height_max):
    visited = [[0]*N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] > height and visited[i][j] == 0:
                visited[i][j] = 1
                cnt += 1
                BFS(i, j)
    result.append(cnt)

print(max(result))
