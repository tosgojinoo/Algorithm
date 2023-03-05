'''
[설명]

[문제]
'''
'''
[알고리즘]

'''
'''
[구조]

'''

'''
- arr 입력
  - M, Z 위치 저장
- BFS
  - M 시작
  - Z 만나면 종료
  - 파이프 모양에 따라 진행
      - 조건문
      - |, - : 각각 수직, 수평으로만 한칸 진행 가능.
      - + : 진행방향으로 한칸 진행. 수직/수평 제한 없음.
      - 1~4 : 90도 방향
  - if '.' 만날 경우
      - 4방 확인
          - 각 방향에서 필요로 하는지 확인. 비트마스크 4bit(좌위우하)
          - 비트마스크를 key로 갖는 dict 에 따라, 파이프 선정
'''

from collections import deque

def BFS():
    global blank_x, blank_y, visited, q

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in pipe_dict[arr[x][y]]:
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<r) or not (0<=ny<c) or visited[nx][ny]: # 제한 조건: 범위, 방문 여부
                continue
            if arr[nx][ny] == "M" or arr[nx][ny] == "Z": # 제한 조건: 시작, 끝
                continue
            if arr[nx][ny] == '.':
                blank_x = nx
                blank_y = ny
            else:
                q.append((nx, ny))


r, c = map(int, input().split())

pipe_dict = {
    "|": [0, 2],
    "-": [1, 3],
    '+': [0, 1, 2, 3],
    "1": [1, 2],
    "2": [0, 1],
    "3": [0, 3],
    "4": [2, 3],
}
visited = [[False] * c for _ in range(r)]
arr = []
start = []
q = deque()
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    arr.append(list(input()))
    for j in range(c):
        if arr[i][j] == "M" or arr[i][j] == "Z":
            visited[i][j] == True
            start.append((i, j))

blank_x = 0
blank_y = 0

flag = False

for x, y in start:
    visited[x][y] = True
    # 북 동 남 서
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<r) or not (0<=ny<c) or visited[nx][ny]:
            continue
        if arr[nx][ny] != '.': # 빈 자리 아닐 경우. 이동 가능 방향 q 삽입
            flag = True
            if i == 0 and (arr[nx][ny] == '|' or arr[nx][ny] == '+' or arr[nx][ny] == '1' or arr[nx][ny] == '4'): # 진행 방향에 따라 이동 가능한 case 분류
                q.append((nx, ny))
            if i == 1 and (arr[nx][ny] == '-' or arr[nx][ny] == '+' or arr[nx][ny] == '3' or arr[nx][ny] == '4'):
                q.append((nx, ny))
            if i == 2 and (arr[nx][ny] == '|' or arr[nx][ny] == '+' or arr[nx][ny] == '2' or arr[nx][ny] == '3'):
                q.append((nx, ny))
            if i == 3 and (arr[nx][ny] == '-' or arr[nx][ny] == '+' or arr[nx][ny] == '1' or arr[nx][ny] == '2'):
                q.append((nx, ny))

    if flag: # 이동 가능 flag
        BFS()
        break
pipe = ""
direction = [False] * 4

# 시작~끝 사이 pipe 가 있을 때
if flag:
    # 북0 동1 남2 서3
    for i in range(4):
        nx = blank_x + dx[i]
        ny = blank_y + dy[i]
        if not (0<=nx<r) or not (0<=ny<c):
            continue
        if i == 0 and (arr[nx][ny] == '|' or arr[nx][ny] == '+' or arr[nx][ny] == '1' or arr[nx][ny] == '4'):
            direction[i] = True
        if i == 1 and (arr[nx][ny] == '-' or arr[nx][ny] == '+' or arr[nx][ny] == '3' or arr[nx][ny] == '4'):
            direction[i] = True
        if i == 2 and (arr[nx][ny] == '|' or arr[nx][ny] == '+' or arr[nx][ny] == '2' or arr[nx][ny] == '3'):
            direction[i] = True
        if i == 3 and (arr[nx][ny] == '-' or arr[nx][ny] == '+' or arr[nx][ny] == '1' or arr[nx][ny] == '2'):
            direction[i] = True

    # 4방이 원하는 형태를 반영하여 pipe 모양 선정
    if direction[0] and direction[2] and not direction[1] and not direction[3]:
        pipe = "|"
    if direction[1] and direction[3] and not direction[0] and not direction[2]:
        pipe = "-"
    if direction[0] and direction[1] and direction[2] and direction[3]:
        pipe = "+"
    if direction[1] and direction[2] and not direction[0] and not direction[3]:
        pipe = "1"
    if direction[0] and direction[1] and not direction[2] and not direction[3]:
        pipe = "2"
    if direction[0] and direction[3] and not direction[1] and not direction[2]:
        pipe = "3"
    if direction[2] and direction[3] and not direction[0] and not direction[1]:
        pipe = "4"
else: # 시작~끝 사이 pipe 가 없을 때
    if start[0][0] == start[1][0]: # 시작, 끝의 행만 확인. 같은 행일 경우
        pipe = "-"
        blank_x = start[0][0]
        blank_y = (start[0][1] + start[1][1]) // 2
    else:
        pipe = "|"
        blank_x = (start[0][0] + start[1][0]) // 2
        blank_y = start[0][1]
print(blank_x + 1, blank_y + 1, pipe)