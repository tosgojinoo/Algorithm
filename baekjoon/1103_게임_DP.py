# H구멍, NxM 보드
# DP memory
#   - 해당 node에서 최대 이동거리 저장
# visited와 DP memory는 무조건 분리
# visited
#   1) DFS 용
#   2) 1step 처리 전후로 상태 변경 및 원복
# 종료조건 종류
#   1) visited가 True인 경우
#   2) DP 값이 이미 있는 경우
#   3) 범위 벗어날 경우
#   4) 강제종료 조건 값일 경우
# DP memory에 한번 값이 저장되면, 이후 overwrite은 금지

import sys
sys.stdin.readline
sys.setrecursionlimit(10000)

def DFS_DP(y, x):
    global state
    if not(0<=y<N and 0<=x<M) or arr[y][x] == 'H': # 이동 종료 조건
        return 0
    if visited[y][x]: # 이동 종료 조건에 걸리지 않고, 방문한 곳에 재방문 시, 무한루프 flag ON
        state = True
        return -1
    if DP[y][x] != -1: # DP가 이미 update 된 경우 return. 이 조건 미포함시, 시간초과.
        return DP[y][x]

    visited[y][x] = True
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        DP[y][x] = max(DP[y][x], DFS_DP(y+dy*int(arr[y][x]), x+dx*int(arr[y][x]))+1) # return 이 아니라 여기에 +1을 넣어줘야 함. 다음 지점의 DP값 + 1(다음 지점으로 1회 이동)
        if state: # 종료조건(무한루프)
            return -1
    visited[y][x] = False

    return DP[y][x]

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[False]*M for _ in range(N)] # DFS용 visited. 1 step 처리 전후로 상태 변경 및 원복.
DP = [[-1]*M for _ in range(N)]
state = False # 무한루프 flag
print(DFS_DP(0, 0))

'''
def DFS_DP(y, x):
    global state
    if not(0<=y<N and 0<=x<M) or arr[y][x] == 'H':
        return 0
    if visited[y][x]:
        state = True
        return -1
    if DP[y][x] != -1:
        return DP[y][x]

    visited[y][x] = True
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        DP[y][x] = max(DP[y][x], DFS_DP(y+dy*int(arr[y][x]), x+dx*int(arr[y][x]))+1) # return 이 아니라 여기에 +1을 넣어줘야 함
        if state:
            return -1
    visited[y][x] = False

    return DP[y][x]

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[False]*M for _ in range(N)]
DP = [[-1]*M for _ in range(N)]
state = False
print(DFS_DP(0, 0))


import sys

sys.setrecursionlimit(10**6)

def DFS_DP(i, j):
    global state
    if not(0<=i<N and 0<=j<M) or arr[i][j] == 'H':
        return 0
    if visited[i][j]:
        state = True
        return -1
    if DP[i][j] != -1:
        return DP[i][j]

    visited[i][j] = True
    multiple = int(arr[i][j])
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        DP[i][j] = max(DP[i][j], DFS_DP(i+di*multiple, j+dj*multiple))
        if state:
            return -1
    visited[i][j] = False

    return DP[i][j]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
DP = [[-1]*M for _ in range(N)]
state = False
print(DFS_DP(0, 0))






틀림
# input = sys.stdin.readline
def DFS_DP(y, x):
    if DP[y][x] != -1:
        return DP[y][x]
    if 
        
    visited[y][x] = True
    multiple = int(arr[y][x])

    if not visited[y][x]:
        ans = 0
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + multiple * dy, x + multiple * dx
            if 0<=ny<N and 0<=nx<M and arr[ny][nx] != 'H':
                ans = max(ans, DFS_DP(ny, nx)+1)
            else:
                continue
        DP[y][x] = ans


    return DP[y][x]

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input()))
DP=[[-1]*M for _ in range(N)]
visited =[[False]*M for _ in range(N)]
print(DFS_DP(0,0))
# print(DP)
'''