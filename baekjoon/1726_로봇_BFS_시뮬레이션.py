# Go k(1~3), Turn dir(L or R)
# 동1, 서2, 남3, 북4
# BFS()
#   - (y, x, dir, cnt)를 q로 관리
#   - 목적지에 도착하는 순간 cnt 출력
#   - 1~3회 직진을 동일 cnt에서 수행
# ***** visited[y][x][4방향]
from sys import stdin
from collections import deque
input = stdin.readline

# 동 서 남 북
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)
change_dir = ((2, 3), (2, 3), (0, 1), (0, 1)) # 동->남/북, 서->남/북, 남->동/서, 북->동/서

def BFS():
    visited = [[[0] * 4 for _ in range(N)] for _ in range(M)]
    visited[sy-1][sx-1][sd-1] = 1
    q = deque([(sy-1, sx-1, sd-1, 0)])
    while q:
        y, x, d, cnt = q.popleft()
        if (y, x, d) == (gy-1, gx-1, gd-1): # (목표위치와 방향)에 도착하면 cnt 리턴
            return cnt

        for forward in range(1, 4):
            ny = y + dy[d] * forward
            nx = x + dx[d] * forward
            nd = d
            if not (0 <= ny < M and 0 <= nx < N) or arr[ny][nx]: # 종료 조건: 벽 or 범위 밖
                break
            if visited[ny][nx][nd]: # 방문 기록 있을 경우 무시
                continue
            q.append((ny, nx, nd, cnt+1))
            visited[ny][nx][nd] = 1

        # 방향 바꾸기
        for nd in change_dir[d]:
            if visited[y][x][nd]:
                continue
            q.append((y, x, nd, cnt+1))
            visited[y][x][nd] = 1

# main
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
sy, sx, sd = map(int, input().split())
gy, gx, gd = map(int, input().split())

print(BFS())