''' my idea
# 3055 방식으로, 단일 queue 처리 고민하기
-> 불만 우선 실행할 경우 시간초과 가능성 있음 => 한 time에 불, 상근이 둘다 계산 필요
1. 불만 BFS
    - memory에 min(level) 저장
2. 상근 BFS
    - not 0<=(y,x)<N 이면, print(level)
    - (y,x)에 도착시
        - level >= memory[y][x] 면 print("impossible")
        - 아니면, continue
'''

'''
BFS
- 불 이동 계산
    - arr 직접 변경
- 상근이 이동 계산
    - visited 저장
'''

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS():
    cnt = 0  # 시간 경과
    while queue: # 상근이 위치
        cnt += 1
        # 불 위치 우선 계산
        while fire and fire[0][2] < cnt: # 다음 time의 불 정보는 미처리
            x, y, time = fire.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] == "." or arr[nx][ny] == "@":
                        arr[nx][ny] = "*"
                        fire.append((nx, ny, time + 1))

        while queue and queue[0][2] < cnt:
            # 상근이 위치 계산
            x, y, time = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] == "." and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, time + 1))
                else: # 탈출 완료
                    return cnt

    return "IMPOSSIBLE"

t = int(input())
for _ in range(t):
    W, H = map(int, input().split())

    queue = deque()  # 상근이의 위치
    fire = deque()  # 불의 위치

    arr = []
    visited = [[False] * W for _ in range(H)]
    for i in range(H):
        arr.append(list(input()))
        for j in range(W):
            if arr[i][j] == "@": # 불 위치 저장
                visited[i][j] = True
                queue.append((i, j, 0)) # y, x, time
            elif arr[i][j] == "*": # 상근 위치 저장
                fire.append((i, j, 0))

    print(BFS())