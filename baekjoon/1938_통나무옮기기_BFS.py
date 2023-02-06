# BFS, 시뮬레이션
# 최소횟수
# 가운데를 기준으로 탐색. 양옆 확인 후 이동 or 회전. 회전은 양옆만 대각선 이동.
# ***** visited: 수직/수평 표기 차원 추가하여 3차원 관리
# q 종료할때까지 ans가 INF 면 0 출력 -> x -> BFS 이므로, 가장 먼저 나오는 cnt 출력
# *** 시작 정보 + 수직/수평 + cnt -> deque -> BFS 활용

from collections import deque
import sys
input = sys.stdin.readline
# 상하좌우, +/-90도 회전
dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
def check(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != "1":
            continue
        else: return False
    return True
def BFS():
    while b:
        x, y, d, cnt = b.popleft()
        if x == ex and y == ey and d == ed:
            return cnt
        # 상하좌우 수평이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if d == 0: # 수평일 때
                # 3지점 범위 내 and 방문 확인
                if 0 <= nx < N and 0 <= ny < N and 0 <= ny - 1 < N and 0 <= ny + 1 < N and visited[nx][ny][0] == 0:
                    if arr[nx][ny] != "1" and arr[nx][ny - 1] != "1" and arr[nx][ny + 1] != "1": # 3개지점 막혔는지 확인
                        visited[nx][ny][0] = 1
                        b.append([nx, ny, 0, cnt + 1])
            elif d == 1: # 수직일 때
                if 0 <= nx < N and 0 <= nx - 1 < N and 0 <= nx + 1 < N and 0 <= ny < N and visited[nx][ny][1] == 0:
                    if arr[nx][ny] != "1" and arr[nx - 1][ny] != "1" and arr[nx + 1][ny] != "1":
                        visited[nx][ny][1] = 1
                        b.append([nx, ny, 1, cnt + 1])

        d = 0 if d == 1 else 1 # d, 방향 전환. 회전.
        # 역방향 진행 전 8방향 and 역방향 방문 확인
        if check(x, y) and visited[x][y][d] == 0:
            visited[x][y][1] = 1
            b.append([x, y, d, cnt + 1])
    return 0
N = int(input())
arr = []
b = deque() # b 를 바로 BFS 까지 연계 사용
e = []
visited = [[[0 for _ in range(2)] for _ in range(N)] for _ in range(N)] # 수직/수평 상태 차원 추가
for i in range(N):
    a = list(input().strip())
    arr.append(a)
    for j in range(N):
        if a[j] == "B":
            b.append([i, j])
        if a[j] == "E":
            e.append([i, j])
if b[1][1] - b[0][1] == 1: # 시작시, 수평일 경우
    b.append([b[1][0], b[1][1], 0, 0]) # 가운데점 x,y, 수직/수평, cnt
else: # 시작시, 수직일 경우
    b.append([b[1][0], b[1][1], 1, 0])

# BFS 종료조건 생성
if e[1][1] - e[0][1] == 1: # 종료 지점이, 수평일 경우
    ex, ey, ed = e[1][0], e[1][1], 0
else: # 종료 지점이, 수직일 경우
    ex, ey, ed = e[1][0], e[1][1], 1

for _ in range(3):
    b.popleft() # 초기 위치값 제거

visited[b[0][0]][b[0][1]][b[0][2]] = 1 # [가운데점 y,x][수직표기]
print(BFS())