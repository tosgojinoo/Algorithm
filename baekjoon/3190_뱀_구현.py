'''
[설명]
사과를 먹으면 뱀 길이가 늘어난다 -> 탐색, DP, 최단경로 아님 -> BFS/DFS x, DP x, Dijkstra x -> deque 활용
벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다
NxN 정사각 보드
몇몇 칸에는 사과
상하좌우 끝에 벽
시작할때 뱀은 맨위 맨좌측에 위치
뱀의 길이는 1
뱀은 처음에 오른쪽
뱀은 매 초마다 이동
1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
    즉, 몸길이는 변하지 않는다.
X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전 -> dxy 순서 제한(동, 남, 서, 북). 시작 동쪽. 회전은 +/-90도만.
[문제]
게임이 몇 초에 끝나는지 출력
'''
'''
[알고리즘]
- deque
    - 성장형
    - 탐색, DP, 최단경로 아님 -> BFS/DFS x, DP x, Dijkstra x
- dxy 순서 제한
    - (동, 남, 서, 북) 순서
    - 시작 동쪽
    - 회전은 +/-90도만.
- turn 
    - (direction - 1) % 4 or
    - (direction + 1) % 4
- while 안에 cnt를 넣고, 한턴 지날때 마다 증가시키며 조건이 되면 turn
'''
'''
[구조]
- arr 저장
- dirDict 저장
- 뱀의 몸 
    - queue = deque([(0, 0)])
    - 성장하기 때문
- while True:
    - cnt, y, x 증가
    - 종료 조건: if not 범위 안
    - if 사과:
        - 뱀으로 채움
        - queue 추가
        - if cnt in dirDict: # 시간 조건이 걸리면
            - turn        
    - elif 아무것도 아님
        - 뱀으로 채움
        - queue 추가
        - queue.popleft() -> 0 처리
        - if cnt in dirDict: # 시간 조건이 걸리면
            - turn
            
- turn 
    - 'L'이면
        - -90도
    - 아니면
        - 90도
'''

# (1, 1) 시작, 길이 1, 맨처음 오른쪽 이동
# 이동한 자리에
#   - 사과가 있으면, 꼬리 고정 + 머리 이동
#   - 사과가 없으면, 꼬리 사라짐 + 머리 이동 (몸길이 고정)



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
    arr[a - 1][b - 1] = 2 # 사과
y, x = 0, 0  # 출발
arr[y][x] = 1 # 뱀

# 방향 정보 저장
L = int(input())
dirDict = dict()
for i in range(L):
    X, C = input().split() # X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전
    dirDict[int(X)] = C

# 동, 남, 서, 북 / 90도 회전 순서 반영
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

cnt = 0 # 시간 증가분
direction = 0 # 시작시 우측 진행. dy, dx 반영.
queue = deque([(0, 0)]) # 뱀의 몸

while True:
    cnt += 1
    y += dy[direction]
    x += dx[direction]

    if not 0<=x<=N-1 or not 0<=y<=N-1: # 종료 조건: 범위 제한
        break

    if arr[y][x] == 2: # 사과일 경우
        arr[y][x] = 1 # 뱀
        queue.append((y, x))
    elif arr[y][x] == 0: # 아무것도 아닐 경우
        arr[y][x] = 1 # 뱀
        queue.append((y, x))
        ty, tx = queue.popleft() # 꼬리 pop
        arr[ty][tx] = 0
    else:
        break

    if cnt in dirDict:
        turn(dirDict[cnt])

print(cnt)