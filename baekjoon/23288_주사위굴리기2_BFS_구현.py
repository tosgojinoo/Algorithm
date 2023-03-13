'''
[설명]
N×M
지도의 오른쪽은 동쪽, 위쪽은 북쪽
(r, c) r는 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수
가장 왼쪽 위에 있는 칸의 좌표는 (1, 1)
가장 오른쪽 아래에 있는 칸의 좌표는 (N, M)
지도의 위에 주사위 하나
주사위 각 면에는 1 ~ 6
주사위 전개도
  2
4 1 3
  5
  6
주사위 지도 위에 윗 면이 1
동쪽을 바라보는 방향이 3인 상태
놓여져 있는 곳의 좌표는 (1, 1)
지도의 각 칸에도 정수
가장 처음에 주사위의 이동 방향은 동쪽
- 주사위의 이동 한 번
    - 주사위가 이동 방향으로 한 칸 굴러감
        - 만약, 이동 방향에 칸이 없다면,
            - 이동 방향을 반대로 한 다음 한 칸 굴러감
    - 주사위 도착한 칸 (x, y)에 대한 점수 획득
    - 주사위 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정
        - A > B인 경우, 이동 방향을 90도 시계 방향 회전
        - A < B인 경우, 이동 방향을 90도 반시계 방향 회전
        - A = B인 경우, 이동 방향에 변화 없음
- 칸 (x, y)에 대한 점수
    - (x, y)에 있는 정수 B
    - (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C -> BFS. dxy 제한 없음.
        - 이동할 수 있는 칸에는 모두 정수 B
            - B와 C를 곱한 값


[문제]
각 이동에서 획득하는 점수의 합
'''
'''
[알고리즘]
- visited
    - BFS 외부에 구성
    - 누적 점수 계산하는데 이전에 사용했다면, 이후 방문에서 제외해야함
- BFS
    - 동일값 갖는 좌표들 따로 저장
    - BFS 탐색 끝난 후, 동일값 좌표들에 동일 score update
- 주사위 진행 방향
    - d = 남 0, 동 1, 북 2, 서 3 로 세팅
    - +/- 90 전환 조건시
        - (d +/- 1)%4 
    - 180 전환 조건시
        - (d + 2)%4
- roll()
    - dice.copy 본을 준비해서 덮어 씌우기
    - 방향
        - 항상 회전은 (x % 총개수)로 계산
        - 남 0
            - 양옆 변경 없음
            - dice[0~3] -1씩 쉬프트((i-1)%4)
        - 북 2
            - 양옆 변경 없음
            - dice[0~3] +1씩 쉬프트((i+1)%4)
        - 동 1 / 서 3
            - dice idx (0, 2, 4, 5) 서로 위치 변경. 바닥, 위, 서, 동
'''
'''
[구조]
- dyx. 제한 없음.
- arr 저장
- score = arr 동일 사이즈. 스코어 저장용.
- visited = arr 동일 사이즈.
- for 전체 탐색:
    - if 방문: 무시
    - BFS(y, x) # 칸별 스코어 미리 계산. 인접 & 동일값은 동일 score. 

- dice = [6, 5, 1, 2, 4, 3] # 주사위. 바닥, 남, 위, 북, 서, 동. idx 무관. 편의상 밑바닥을 idx 0, 나머지는 순서대로.

- (0, 0) 시작 지점
- d = 1 동쪽 방향

- for 이동횟수:
    - y/x += dxy
    - if 범위 밖:
        - d = (d+2)%4 # 반대방향 전환
        - y/x += dxy
    - roll(d) # 주사위 돌림
    - score를 result에 추가
    - if 주사위 아랫면 정수가, arr보다 더 클 경우:
        - d = (d-1)%4 # 90도 시계방향 회전
    - elif 주사위 아랫면 정수가, arr 보다 더 작을 경우:
        - d = (d+1)%4 # 90도 반시계방향 회전

- print(result)

- BFS(y, x):
    - target_num = 기준값
    - same_nums = 동일값 같는 좌표들
    - queue = deque([(y, x)])
    - while queue:
        - if 방문: 무시
        - 방문처리
        - same_nums.append((y, x))
        - for 4방향:
            - if 범위 내:
                - if 기준값과 동일값:
                    - queue.append((ny, nx))
    - for same_nums 에서 하나씩 확인:
        - score[y][x] = target_num * len(same_nums)


- def roll(d):
    newdice = dice.copy 준비(편의상)
    if d == 0:# 남
        for i in range(4):
            newdice[(i-1)%4] = dice[i]
    elif d == 1: # 동
        newdice[0] = dice[5]
        newdice[5] = dice[2]
        newdice[2] = dice[4]
        newdice[4] = dice[0]
    elif d == 2: # 북
        for i in range(4):
            newdice[(i+1)%4] = dice[i]
    else: # 서
        newdice[5] = dice[0]
        newdice[2] = dice[5]
        newdice[4] = dice[2]
        newdice[0] = dice[4]
    return newdice

'''


import sys
input = sys.stdin.readline
from collections import deque


def roll(d):
    newdice = dice[:]
    if d == 0:# 남
        for i in range(4):
            newdice[(i-1)%4] = dice[i]
    elif d == 1: # 동
        newdice[0] = dice[5]
        newdice[5] = dice[2]
        newdice[2] = dice[4]
        newdice[4] = dice[0]
    elif d == 2: # 북
        for i in range(4):
            newdice[(i+1)%4] = dice[i]
    else: # 서
        newdice[5] = dice[0]
        newdice[2] = dice[5]
        newdice[4] = dice[2]
        newdice[0] = dice[4]
    return newdice

def BFS(y, x):
    target_num = arr[y][x]
    same_nums = [] # 동일 값 다른 좌표들
    queue = deque([(y, x)])
    while queue:
        y, x = queue.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = 1 # 방문 처리
        same_nums.append((y, x)) # 동일 값 다른 좌표들
        for i in range(4): # 4방향
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<N and 0<=nx<M: #범위 내
                if arr[ny][nx] == target_num: # 동일 숫자
                    queue.append((ny, nx))
    for y, x in same_nums:
        score[y][x] = target_num * len(same_nums)

dy = [1, 0, -1, 0] # 남, 동, 북, 서. 0, 1, 2, 3.
dx = [0, 1, 0, -1]
N, M, K = map(int, input().split()) # 크기가 N×M, idx 1부터 시작. 이동횟수 K.
arr = [[*map(int, input().split())] for _ in range(N)]
score = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for y in range(N):
    for x in range(M):
        if visited[y][x]:
            continue
        BFS(y, x) # 칸별 스코어 미리 계산. 인접 & 동일 숫자들은 동일 스코어.

dice = [6, 5, 1, 2, 4, 3] # 주사위
'''
  2
4 1 3
  5
  6
'''

y = x = 0
d = 1 # 시작 방향 동쪽
result = 0
for _ in range(K):
    ny, nx = y+dy[d], x+dx[d]
    if not (0<=ny<N and 0<=nx<M): # 범위 밖
        d = (d+2)%4 # 반대방향 전환. d = 남 0, 동 1, 북 2, 서 3
        ny, nx = y+dy[d], x+dx[d]
    y, x = ny, nx
    dice = roll(d) # 주사위 돌림
    result += score[y][x]
    if dice[0] > arr[y][x]: # 주사위 아랫면 정수가 더 클 경우
        d = (d-1)%4 # 90도 시계방향 회전
    elif dice[0] < arr[y][x]: # 작을 경우
        d = (d+1)%4 # 90도 반시계방향 회전

print(result)