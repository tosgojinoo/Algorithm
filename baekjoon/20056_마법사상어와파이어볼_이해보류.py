''' my idea
N, M, K: size, 정보 개수, 이동 명령수
r_i, c_i, m_i, d_i, s_i: 위치r, 위치c, 질량, 방향, 속력 <- M개
'''

from collections import deque

def move_fires():
    check_point = set()
    while fire_pos:
        r, c, m, s, d = fire_pos.pop()
        nr, nc = (r + dr[d] * s) % N, (c + dc[d] * s) % N
        arr[nr][nc].append((m, s, d))
        check_point.add((nr, nc))
    check_fires(check_point)

def check_fires(check_point):
    for x, y in check_point:
        length = len(arr[x][y])
        if length == 1:
            m, s, d = arr[x][y].pop()
            fire_pos.append((x, y, m, s, d))
        elif length >= 2:
            sum_m, sum_s, cnt = 0, 0, 0
            for m, s, d in arr[x][y]:
                sum_m += m
                sum_s += s
                if d % 2 == 0:
                    cnt += 1
            arr[x][y] = deque()
            sum_m //= 5
            sum_s //= length
            if sum_m == 0:
                continue
            dirs = (0, 2, 4, 6) if cnt in (0, length) else (1, 3, 5, 7)
            for d in dirs:
                fire_pos.append((x, y, sum_m, sum_s, d))


dr = [-1, -1, 0, 1, 1, 1, 0, -1] # 8방향. 위 부터 시계방향.
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, F, K = map(int, input().split())
arr = [[deque() for _ in range(N)] for _ in range(N)]

fire_pos = deque()
for _ in range(F):
    r, c, m, s, d = map(int, input().split())
    fire_pos.append((r, c, m, s, d)) # 파이어볼 정보 저장

for _ in range(K):
    move_fires()
answer = 0
for _, _, m, _, _ in fire_pos:
    answer += m
print(answer)