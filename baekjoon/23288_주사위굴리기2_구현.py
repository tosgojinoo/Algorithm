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
    cnt = 0
    target_num = arr[y][x]
    same_nums = []
    queue = deque([(y, x)])
    while queue:
        y, x = queue.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = 1 # 방문 처리
        cnt += 1
        same_nums.append((y, x))
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<N and 0<=nx<M: #범위 내
                if arr[ny][nx] == target_num: # 동일 숫자
                    queue.append((ny, nx))
    for y, x in same_nums:
        score[y][x] = target_num * cnt

dy = [1, 0, -1, 0] # 남, 동, 북, 서. 0, 1, 2, 3.
dx = [0, 1, 0, -1]
N, M, K = map(int, input().split()) # 크기가 N×M, idx 1부터 시작.
arr = [[*map(int, input().split())] for _ in range(N)]
score = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
# 미리 인접 숫자들에 대한 score 계산
for y in range(N):
    for x in range(M):
        if visited[y][x]:
            continue
        BFS(y, x) # 인접 & 같은 숫자들 계산

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
for i in range(K):
    ny, nx = y+dy[d], x+dx[d]
    if not (0<=ny<N and 0<=nx<M): # 범위 밖
        d = (d+2)%4 # 반대방향 전환
        ny, nx = y+dy[d], x+dx[d]
    y, x = ny, nx
    dice = roll(d) # 주사위 돌림
    result += score[y][x]
    if dice[0] > arr[y][x]: # 주사위 아랫면 정수가 더 클 경우
        d = (d-1)%4 # 90도 시계방향 회전
    elif dice[0] < arr[y][x]: # 작을 경우
        d = (d+1)%4 # 90도 반시계방향 회전

print(result)