# 2곳에 1을 채우는 모든 경우의 수 생성(루프) -> x -> 0 위치를 전부 저장한 후, 2개씩 조합 생성하여 1로 변경 후 BFS
# arr 생성
#   - 2 위치만 따로 저장하는 pos 생성
# 지나가다가 2를 만나면 BFS
#   - 상하좌우
#   - 0을 만나면 종료
#   - 2만 전부 cnt, 추가 및 저장
# 다시 2 탐색 후 BFS 반복
# 한 판이 끝니면 초기화. cnt = max(cnt, solve())

import sys

input = sys.stdin.readline
from collections import deque

def comb(arr, r):
    for i in range(len(arr)):
        if r == 1: # 종료 조건
            yield [arr[i]]
        else:
            for nxt in comb(arr[i+1:], r-1):
                yield [arr[i]] + nxt

def BFS(x, y, visited):
    queue = deque()
    visited[x][y] = True
    queue.append([x, y])
    kill_ai_stone = 1
    flag = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    flag = 1
                elif arr[nx][ny] == 2:
                    visited[nx][ny] = True
                    kill_ai_stone += 1
                    queue.append([nx, ny])
    return kill_ai_stone if not flag else -1


def solve(put_stone):
    visited = [[False] * M for _ in range(N)]
    kill_count = 0
    for x, y in put_stone:
        arr[x][y] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2 and not visited[i][j]:
                cnt = BFS(i, j, visited)
                if cnt != -1:
                    kill_count += cnt
    for x, y in put_stone:
        arr[x][y] = 0
    return kill_count


N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

arr = []
pos = [] # 0 위치 따로 저장
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(M):
        num = row[j]
        if not num:
            pos.append((i, j))

cnt = 0
for my_turn in comb(pos, 2): # 0 위치 중 2개씩 조합하여 1로 변경
    cnt = max(cnt, solve(my_turn))
print(cnt)