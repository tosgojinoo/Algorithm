'''
[설명]
오른쪽은 동쪽, 위쪽은 북쪽
지도의 위에 주사위 하나
주사위의 전개도
  2
4 1 3
  5
  6
지도의 좌표는 (r, c)
r는 북쪽으로부터 떨어진 칸의 개수
c는 서쪽으로부터 떨어진 칸의 개수

주사위는 지도 위에 윗 면이 1
동쪽을 바라보는 방향 3
놓여져 있는 곳의 좌표는 (x, y)

가장 처음에 주사위에는 모든 면에 0 -> 초기값
지도의 각 칸에는 정수
이동한 칸에 쓰여 있는 수 0 이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사 -> 반영
이동한 칸에 쓰여 있는 수 0 아니면, 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사, 칸에 쓰여 있는 수는 0 -> 반영

주사위를 바깥으로 이동시키려고 하는 경우, 해당 명령 무시, 출력 x -> command 반영

주사위를 놓은 칸에 쓰여 있는 수는 항상 0 -> 주사위 시작점의 arr 값
지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0 -> 0<= arr <=9
동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4 -> dxy

[문제]
이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력 -> 윗면 idx 확인
'''
'''
[알고리즘]
- dxy 제한 없음
- command:
    - 범위 밖 이동 -> 무시, 출력 x
- turn()
    - 주사위 6면의 idx를 정의한 순서대로 적용 계산
    - 4방향별 idx 배열 구성
'''
'''
[구조]
- dice 6면, dxy, 
- arr, commands 저장
- for cmd in commands:
    - nxy += dxy[cmd-1] 
    - if 범위 제한
        - 출력 x. nxy 원복. 무시.
    - turn(cmd)
    - if arr 값이 0:
        - arr = dice[-1] # 주사위 밑면 값 복사
    - else: 
        - dice[-1], arr = arr, 0 # 주사위 밑면에 칸의 값 복사. 칸은 0.
- turn(direction)
    - a,b,c,d,e,f = dice 6면
    - if direction
        - dice 재구성
'''
def turn(direction):
    global dice
    a, b, c, d, e, f = dice
    if direction == 1: # 동
        dice = [d, b, a, f, e, c]

    elif direction == 2: # 서
        dice = [c, b, f, a, e, d]

    elif direction == 3: # 북
        dice = [e, a, c, d, f, b]

    else:
        dice = [b, f, c, d, a, e]

# 세로 N, 가로 M (1 ≤ N, M ≤ 20)
# 주사위를 놓은 곳의 좌표 x, y (0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1)
# 명령 K (1 ≤ K ≤ 1,000)
N, M, X, Y, K = map(int, input().split())

dx = [0, 0, -1, 1] # 동, 서, 북, 남. idx -1 적용.
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0] # 6면 값 초기화 / idx 0이 초기 윗면, idx 5가 밑면

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

nx, ny = X, Y
for cmd in commands:
    nx += dx[cmd-1] # idx -1 반영
    ny += dy[cmd-1]

    if not 0<=nx<N or not 0<=ny<M: # 종료 조건: 범위 제한. 출력 x. 무시함.
        nx -= dx[cmd-1] # 원복. 무시.
        ny -= dy[cmd-1]
        continue
    turn(cmd)

    if not arr[nx][ny]: # 칸의 값이 0일때
        arr[nx][ny] = dice[-1] # 주사위 밑면 값 복사
    else: # 칸의 값이 0이 아닐때
        dice[-1], arr[nx][ny] = arr[nx][ny], 0 # 주사위 밑면에 칸의 값 복사. 칸은 0.

    print(dice[0])