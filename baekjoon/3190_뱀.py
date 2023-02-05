# (1, 1) 시작, 길이 1, 맨처음 오른쪽 이동
# 이동한 자리에
#   - 사과가 있으면, 꼬리 고정 + 머리 이동
#   - 사과가 없으면, 꼬리 사라짐 + 머리 이동 (몸길이 고정)

# DFS/BFS x, DP x, Dijkstra x
# 구현, 자료구조, 시뮬레이션, 덱, 큐


from collections import deque

def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

N = int(input()) # 보드 크기
K = int(input()) # 사과 개수

# init(0), 사과(2), 뱀(1)
arr = [[0] * N for _ in range(N)]
for i in range(K):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 2
y, x = 0, 0
arr[y][x] = 1

# 방향 정보 저장
L = int(input())
dirDict = dict()
for i in range(L):
    X, C = input().split()
    dirDict[int(X)] = C

# 동, 남, 서, 북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

cnt = 0 # 시간 증가분
direction = 0 # 시작시 우측 진행. dy, dx 반영.
q = deque() # 뱀의 몸
q.append((0, 0))

while True:
    cnt += 1
    y += dy[direction]
    x += dx[direction]

    if x < 0 or x >= N or y < 0 or y >= N: # 종료 조건: 범위 제한
        break

    if arr[y][x] == 2: # 사과일 경우
        arr[y][x] = 1 # 뱀
        q.append((y, x))
        if cnt in dirDict:
            turn(dirDict[cnt])

    elif arr[y][x] == 0: # 아무것도 아닐 경우
        arr[y][x] = 1 # 뱀
        q.append((y, x))
        ty, tx = q.popleft() # 꼬리 pop
        arr[ty][tx] = 0
        if cnt in dirDict:
            turn(dirDict[cnt])

    else:
        break

print(cnt)