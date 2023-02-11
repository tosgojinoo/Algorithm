# 1261 알고스팟과 동일

from collections import deque
def BFS():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if arr[nx][ny] == 0: # 검은방
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
                else:
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft([nx, ny]) # 흰방 먼저 방문하기 위해


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)] # 상태값 0 가능하므로, -1 초기화
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

BFS()
print(visited[N-1][N-1])