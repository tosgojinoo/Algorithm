'''
[설명]
Baduk2의 룰은 바둑과 거의 유사
양 선수가 돌을 1개씩 번갈아 두는 것이 아니라 2개씩 둔다는 점이 다름
서술의 편의를 위해 상하좌우로 인접한 같은 색 돌의 집합을 그룹

Baduk2에서는 일반적인 바둑과 동일하게 자신의 돌로 상대방의 그룹을 빈틈없이 에워싸면 갇힌 돌을 죽일 수 있음
어느 그룹이 빈틈없이 에워싸였다는 것은 그 그룹 내에 빈 칸과 인접해있는 돌이 하나도 없다는 것과 동치
Baduk2에서는 모든 비어있는 칸에 돌을 둘 수 있음
설령 상대 돌로 둘러싸여 있어 스스로 잡히는 곳이라고 하더라도 상관이 없음

0은 빈 칸, 1은 나의 돌, 2는 상대의 돌

[문제]
돌 2개를 두어 죽일 수 있는 상대 돌의 최대 갯수
'''
'''
[알고리즘]
- pos
    - 0 위치 별도 관리
- solve()
    - 경우의 수 > put_stone > arr 표기 > BFS > kill_count > arr 원복
- BFS
    - 상대방 돌 그룹이 빈틈없이 둘러쌓였는지 확인
    - 상대방 돌일 경우 BFS 진입
    - BFS 탐색 중 0(빈칸)을 만나면 fail_flag 
    - fail_flag 없이 전부 queue를 탐색 종료해야, 그룹 완성 -> 상대방 돌 kill

'''
'''
[구조]
- arr = 저장
- pos = 0 위치 별도 저장

- for combination(pos, 2):
    cnt = max(cnt, solve(my_turn))
- print(cnt)

- combination(arr, r)

- solve(put_stone):
    - for put_stone:
        - arr[x][y] = 1 돌 놓은 곳 표시
    - for 전체 탐색:
        - if 상대방돌 & 미방문:
            - cnt = BFS(i, j, visited)
            - if cnt != -1:
                - kill_count += cnt (정산)
    - for put_stone:
        - arr[x][y] = 0 원복
    - return kill_count

- BFS(x, y, visited):
    - kill_ai_stone = 1
    - while queue:
        - for 4방향:
            - if 범위 내 and 미방문:
                - if arr[nx][ny] == 0:
                    - fail_flag = 1
                - elif arr[nx][ny] == 2:
                    - visited[nx][ny] 방문처리
                    - kill_ai_stone += 1
                    - queue 추가
    - return kill_ai_stone if not fail_flag else -1
'''



import sys
from collections import deque
input = sys.stdin.readline


def combination(arr, r):
    for i in range(len(arr)):
        if r == 1: # 종료 조건
            yield [arr[i]]
        else:
            for nxt in combination(arr[i+1:], r-1):
                yield [arr[i]] + nxt

def BFS(x, y, visited):
    queue = deque([x, y])
    visited[x][y] = True
    kill_ai_stone = 1
    fail_flag = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    fail_flag = 1
                elif arr[nx][ny] == 2:
                    visited[nx][ny] = True
                    kill_ai_stone += 1
                    queue.append([nx, ny])
    return kill_ai_stone if not fail_flag else -1


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


N, M = map(int, input().split()) # 행의 갯수와 열의 갯수를 나타내는 N(3 ≤ N ≤ 20)과 M(3 ≤ M ≤ 20)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

arr = []
pos = [] # 0 위치 별도 저장
for i in range(N):
    row = list(map(int, input().split())) # 0은 빈 칸, 1은 나의 돌, 2는 상대의 돌
    arr.append(row)
    for j in range(M):
        num = row[j]
        if not num:
            pos.append((i, j))

cnt = 0
for my_turn in combination(pos, 2): # 0 위치 중 2개씩 조합하여 1로 변경
    cnt = max(cnt, solve(my_turn))
print(cnt)