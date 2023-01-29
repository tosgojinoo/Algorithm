# 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데,
# 이때 최단 경로로 이동하려 한다.
# 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데,
# 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면,
# 벽을 한 개 까지 부수고 이동하여도 된다.
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

# arr와 visited 배열을 함께 운영할 수 없음, 그 다음 이동에서 변동된 arr에 영향 받기 때문
# visited 를 0/1 형태로 운영하면, 나중에 방문이 불가능해짐
# "visited & cnt & 상태" 방식으로 운영해야 함
from collections import deque

def BFS():
    q = deque([(0,1,1)]) # z, y, x
    visited[0][1][1] = 1
    visited[1][1][1] = 1
    arr[1][1] = 1
    while q:
        z, y, x = q.popleft() # z == chance to break a wall
        if y==N and x==M:
            return visited[z][y][x]
        for dy, dx in moves:
            ny, nx = y+dy, x+dx
            if 1<=ny<=N and 1<=nx<=M:
                if arr[ny][nx]==1 and z==1:
                    continue
                if arr[ny][nx]==0 and visited[z][ny][nx]==0:
                    visited[z][ny][nx]=visited[z][y][x]+1
                    q.append((z, ny, nx))
                elif arr[ny][nx]==1 and z==0:
                    visited[z+1][ny][nx]=visited[z][y][x]+1
                    q.append((z+1, ny, nx))

    return -1



N, M = map(int, input().split()) # N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)
arr = [[1]*(M+1)]
arr = arr + [[1]+list(map(int, list(input()))) for _ in range(N)]
visited = [[1]*(M+1)]
visited = [visited + [[1]+[0]*M for _ in range(N)] for _ in range(2)]
moves = [(1,0),(-1,0),(0,1),(0,-1)]

cnt = 0
cnt = BFS()
print(cnt)

