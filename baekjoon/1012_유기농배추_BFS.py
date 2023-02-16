# '단지번호 입력'과 유사
from collections import deque

dxy = [(1,0),(-1,0),(0,1),(0,-1)]

def BFS(y, x):
    queue = deque([(y, x)])

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dxy[i][0], x+dxy[i][1]
            if 0<=ny<N and 0<=nx<M and arr[ny][nx]:
                arr[ny][nx]=0
                queue.append((ny, nx))


for _ in range(int(input())):
    M, N, K = map(int, input().split()) # 가로, 세로, 배추 개수
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
           if arr[i][j]:
               arr[i][j] = 0
               cnt += 1
               BFS(i, j)

    print(cnt)