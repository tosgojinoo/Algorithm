# 전체 블록 4방향 이동
# 최대 5번 이동, 가장 큰 블록값


# [순서]
# for 4방향
# deepcopy(arr) 사용
# => *** 시간 줄이기 위해, 4방향 5개조합 추출 후 arr 적용 보다,
# => 바로 arr 적용해서 DFS 넘겨야함

# 이동은 가능할 때 까지
# - * 이동방향에 따라, 먼저 계산하는 순서 다르게 적용(동쪽 이동은 오른쪽부터 계산)
# 블록 합치기
# - 이미 합쳐진 블록이면 합칠수 없음 -> 다른 상태값 -> 한턴에 한번만 합치기 -> 매턴마다 status 초기화
# => ***** 이동, 합치기에 대한 정리 제일 중요
# - 범위 내
# - 0인지 아닌지
# - 동일 숫자 인지 아닌지
# - 이전에 합친 기록이 있는지 없는지



# [종료]
# 이동 5회

# [체크]
# 부루트포스, 가지치기 불가
# 4방향에 대한 5개 조합 모두 생성 필요


# 내답, 느림
from copy import deepcopy

def change_loc(arr, status, y, x, dy, dx):
    ny, nx = y + dy, x + dx
    while True:
        # 외곽까지 이동
        if 0<=ny<N and 0<=nx<N:
            # 0이면 계속 진행
            if arr[ny][nx] == 0:
                arr[ny][nx], arr[y][x] = arr[y][x], 0
                ny, nx, y, x = ny + dy, nx + dx, ny, nx
            else: # 0 아니면
                # 동일 숫자
                if arr[ny][nx] == arr[y][x]:
                    # 합친적이 없으면
                    if not status[ny][nx] and not status[y][x]:
                        arr[ny][nx], arr[y][x] = arr[y][x] * 2, 0
                        status[ny][nx] = True
                        break
                    # 합친적이 하나라도 있으면, 이동 불가
                    else: break
                # 다른 숫자
                else: break
        # 외곽 벗어나면
        else: break
    return arr, status

def DFS(arr_init, cnt):
    global result

    # 5회 이동 조합
    if cnt == 5:
        result = max(result, max(map(max, arr_init)))
        return

    for case in moves:
        # 이동 적용
        dy, dx = case
        arr = deepcopy(arr_init)
        if dy == 1:
            flag1 = -1  # 방향에 따라 먼저 계산해야하는 순서가 바뀜
        else:
            flag1 = 1
        if dx == 1:
            flag2 = -1
        else:
            flag2 = 1

        status = [[False] * N for _ in range(N)]

        for i in list(range(N))[::flag1]:
            for j in list(range(N))[::flag2]:
                if arr[i][j] != 0:
                    arr, status = change_loc(arr, status, i, j, dy, dx)

        DFS(deepcopy(arr), cnt+1)

N = int(input())
arr_init = [list(map(int, input().split())) for _ in range(N)]
moves = [(1,0), (-1,0), (0,1), (0,-1)]
status =[]
result = 0

DFS(arr_init, 0)

print(result)







# 참고
'''
def move(arr, dir):
    if dir == 0:  # 동쪽
        for i in range(N):
            top = N - 1 # top 설정으로 검색 범위 제한할 수 있음, 벽쪽에 가장 근접한 곳은 계산 제외, 합쳐진 곳은 합쳐지기전 두곳 모두 제외
            for j in range(N - 2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][top] == 0:
                        arr[i][top] = tmp
                    elif arr[i][top] == tmp:
                        arr[i][top] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        arr[i][top] = tmp

    elif dir == 1:  # 서쪽
        for i in range(N):
            top = 0
            for j in range(1, N):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][top] == 0:
                        arr[i][top] = tmp
                    elif arr[i][top] == tmp:
                        arr[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        arr[i][top] = tmp

    elif dir == 2:  # 남쪽
        for j in range(N):
            top = N - 1
            for i in range(N - 2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[top][j] == 0:
                        arr[top][j] = tmp
                    elif arr[top][j] == tmp:
                        arr[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        arr[top][j] = tmp

    else:
        for j in range(N):
            top = 0
            for i in range(1, N):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[top][j] == 0:
                        arr[top][j] = tmp
                    elif arr[top][j] == tmp:
                        arr[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        arr[top][j] = tmp

    return arr


def DFS(arr, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, arr[i][j])
        return

    for i in range(4):
        arr_tmp = move(deepcopy(arr), i)
        DFS(arr_tmp, cnt + 1)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
DFS(arr, 0)
print(ans)
'''

