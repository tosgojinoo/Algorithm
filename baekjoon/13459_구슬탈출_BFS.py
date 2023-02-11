''' my idea

BFS()
- queue = deque([y, x, cnt])
- whiel queue:
    - for i in range(4):
        - nx, ny = x/y + dxy
        - if 0<=nx, xy<N/M and not visited[ny,nx]:
            - if '.':
                - queue.append()
            - if 'H':
                continue
            - if '0': # 구멍
                return


main
- blue
- red
- arr
    if 'B'
        blue = [y,x]
    if 'R'
        red = [y,x]

'''

from sys import stdin
from collections import deque

input = stdin.readline

def move(x, y, dx, dy):
    count = 0  # 이동한 칸 수
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while arr[x + dx][y + dy] != '#' and arr[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def BFS():
    global rx, ry, bx, by
    queue = deque()
    queue.append((rx, ry, bx, by, 1)) # 위치, depth
    visited[rx][ry][bx][by] = True

    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:  # 제한 조건
            break
        for i in range(4):
            nrx, nry, r_count = move(rx, ry, dx[i], dy[i])  # RED
            nbx, nby, b_count = move(bx, by, dx[i], dy[i])  # BLUE

            if arr[nbx][nby] == 'O':  # 파란 구슬이 구멍에 떨어지지 않으면(실패 X)
                continue
            if arr[nrx][nry] == 'O':  # 빨간 구슬이 구멍에 떨어진다면(성공)
                print(1)
                return
            if nrx == nbx and nry == nby:  # 동시 같은 칸 일 경우
                if r_count > b_count:  # 이동 거리가 많은 구슬을 한칸 뒤로
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth + 1))
    print(0)  # 실패

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)] # 상태 차원 rx * ry * bx * by
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
rx, ry, bx, by = [0] * 4
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':  # red 저장
            rx, ry = i, j
        elif arr[i][j] == 'B':  # blue 저장
            bx, by = i, j
BFS()