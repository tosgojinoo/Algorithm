# visited. 3차원. [수직층][y][x]
# cnt
# state. N개. 각 층별 회전 횟수 -> x
# rotate() 회전시 해당층 재배열
# 층별로 회전은 DFS -> 그냥 각 층 회전하며 루프
# 최소 이동 BFS
# 이동은 상하를 포함한 6방향
# 판 쌓는 순서 조합. yield로 구성

import sys
from collections import deque

def perms(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in perms(arr[:i]+arr[i+1:], r-1):
                yield [arr[i]] + nxt

def rotate(arr_one):
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(len(arr_one)):
        for j in range(len(arr_one[0])):
            tmp[j][4 - i] = arr_one[i][j]

    return tmp

def BFS(arr):  # 시작부터 끝까지 이동
    global result
    visited = [[[0, 0, 0, 0, 0] for _ in range(5)] for _ in range(5)] # visitied == visited & cnt
    q = deque()
    q.append((0, 0, 0))

    while q:
        h, y, x = q.popleft()
        if (h, y, x) == (4, 4, 4):
            result = min(result, visited[4][4][4])
            if result == 12: # 가장 짧은 경로의 경우 출력 후 종료
                print(result)
                exit()
            return

        for i in range(6):
            nh = h + dh[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if nh < 0 or nh >= 5 or ny < 0 or ny >= 5 or nx < 0 or nx >= 5: # 제한 조건: 범위
                continue
            elif arr[nh][ny][nx] == 0 or visited[nh][ny][nx] != 0: # 제한 조건: 방문했거나, 갈 수 없는 곳
                continue
            q.append((nh, ny, nx))
            visited[nh][ny][nx] = visited[h][y][x] + 1

def DFS(step): # 시작과 끝 조건만 부합하는 case 생성 -> BFS
    global arr
    if step == 5:
        if arr[4][4][4]: # (4,4,4) 가 종료 조건에 만족하면
            BFS(arr)
        return

    for i in range(4):
        if arr[0][0][0]: # (0,0,0) 이 시작 조건에 만족하는 모든 경우에 DFS
            DFS(step + 1)
        arr[step] = rotate(arr[step]) # 회전하며 다음 경우의 수 생성

def solve(): # 판 쌓는 순서 조합 생성 -> DFS
    for d in perms([0, 1, 2, 3, 4], 5): # 판 쌓는 순서 조합
        for i in range(5):
            arr[d[i]] = arr_init[i]
        DFS(0)


arr_init = [[list(map(int, input().split(' '))) for _ in range(5)] for _ in range(5)]
arr = [[[0] * 5 for _ in range(5)] for _ in range(5)]
result = sys.maxsize

# 상하좌우앞뒤 6방향 이동
dh = (0, 0, 0, 0, 1, -1)
dy = (0, 0, 1, -1, 0, 0)
dx = (1, -1, 0, 0, 0, 0)
solve()

if result == sys.maxsize:
    result = -1
print(result)