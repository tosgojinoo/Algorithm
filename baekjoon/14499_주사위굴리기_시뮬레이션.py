# NxM 지도
# 지도 좌표 (r, c) / r: 북쪽에서부터의 칸 수, c: 서쪽에서부터의 칸 수
# 주사위 모든면 초기값 0
# ***** turn 함수 정의
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

N, M, X, Y, K = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0] # 6면 값 초기화 / index 0이 초기 윗면, index 5가 밑면

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

order = list(map(int, input().split()))

nx, ny = X, Y
for i in order:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= N or ny < 0 or ny >= M: # 종료 조건: 범위 제한. 출력 x. 무시함.
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)

    if arr[nx][ny] == 0: # 칸의 값이 0일때
        arr[nx][ny] = dice[-1] # 주사위 밑면 값 복사
    else: # 칸의 값이 0이 아닐때
        dice[-1] = arr[nx][ny] # 주사위 밑면에 칸의 값 복사
        arr[nx][ny] = 0 # 칸은 0

    print(dice[0])