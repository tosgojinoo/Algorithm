# padding
# BFS
#   - q.append([y,x,cnt])
#   - visited[문 on/off][y][x] -> *** state: 문 0/1/2 on
#   - prisons = 0
#   - if 문 on: cnt+=1
#   - ans = min(ans, cnt)
#   - if $:
#       - prisons += 1
#   - if prisons == 2:
#       print(cnt)
#       exit()

import sys
from collections import deque

def BFS(y, x):
    visited = [[-1] * (W + 2) for _ in range(H + 2)]  # padding. 열어야하는 문 개수 기록
    queue = deque()
    queue.append([y, x])
    visited[y][x] = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny <= H + 1 and 0 <= nx <= W + 1: # 범위 내
                if visited[ny][nx] == -1: # 미방문
                    if board[ny][nx] == '.' or board[ny][nx] == '$':  # 문을 안열고 진행
                        visited[ny][nx] = visited[y][x]
                        queue.appendleft([ny, nx])  # 가장 앞에 삽입(우선 처리)
                    elif board[ny][nx] == '#':  # 문을 여는 경우
                        visited[ny][nx] = visited[y][x] + 1 # 문 연 개수 추가
                        queue.append([ny, nx])
    return visited


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

tc = int(input())
for _ in range(tc):
    H, W = map(int, input().split())
    board = [list('.' * (W + 2))]  # 맨 윗줄 추가
    for i in range(H):
        board.append(list('.' + input().strip() + '.'))
    board.append(list('.' * (W + 2)))  # 맨 아랫줄 추가

    prisoner = []
    for i in range(H + 2):
        for j in range(W + 2):
            if board[i][j] == '$':
                prisoner.append([i, j])

    one = BFS(*prisoner[0]) # 첫번째 죄수 ~ (0,0) 까지 필요한 문 개수
    two = BFS(*prisoner[1]) # 두번째 죄수 ~ (0,0) 까지
    zero = BFS(0, 0) # (0,0) ~ 모든 곳 도착
    answer = sys.maxsize

    for y in range(H + 2):
        for x in range(W + 2):
            if one[y][x] != -1 and two[y][x] != -1 and zero[y][x] != -1: # 모든 경우에서 update 됐을 경우
                result = one[y][x] + two[y][x] + zero[y][x]  # 해당 위치에서 문을 여는 개수
                if board[y][x] == '*':  # 벽은 제외
                    continue
                if board[y][x] == '#':  # 한명만 열어도 되기 때문에 나머지 사람이 연 갯수인 2를 빼줌
                    result -= 2
                answer = min(answer, result)
    print(answer)