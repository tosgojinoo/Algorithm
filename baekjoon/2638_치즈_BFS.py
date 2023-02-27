from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def BFS():
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny]:
                    melt[(nx, ny)] += 1
                else: # arr == 0 만 visited 처리
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

time = 0
while True:
    visited = [[0]*M for _ in range(N)]
    melt = defaultdict(lambda: 0)
    BFS()
    flag = False
    for i, j in melt:
        if melt[(i, j)] >= 2: # 공기와 2회 이상 접촉시
            arr[i][j] = 0 # 삭제
            flag = True
    if flag:
        time += 1
    else:
        break

print(time)