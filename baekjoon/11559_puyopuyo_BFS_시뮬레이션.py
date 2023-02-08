# 가장 밑에 줄부터 탐색 시작
# 모든 지점에서 BFS 시작
#   - 동일 색에 대해서만 visited
#   - 더이상 진전 불가할 때까지 cnt
# cnt_BFS가 4 이상일 경우 visited 1인 모든 요소 '.' 으로 변환 -> 함수
# *** 한 턴에 BFS는 될 때까지 계속 수행
# cnt_clear += 1
# 변환 후 하단으로 요소 위치 이동, 맵 갱신 -> 함수 => 뿌요가 있을 경우 q에 우선 기록, 아래에서부터 q에 있는 요소를 먼저 뿌려주면 update 가능
# if '.' 개수 확인: 12*6개면 종료
# else: 다시 탐색 시작
# 모든 탐색이 종료되면, cnt_clear 출력

from collections import deque

def BFS(y, x, value):
    q = deque()
    q.append((y, x))

    clear_target = deque() # clear_target
    clear_target.append((y, x))

    visited = [[False] * 6 for _ in range(12)]
    visited[y][x] = True
    cnt = 1
    flag = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny > 11 or nx < 0 or nx > 5:
                continue
            if arr[ny][nx] == value and not visited[ny][nx]:
                q.append((ny, nx))
                clear_target.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1

    if cnt >= 4:
        flag = 1

        for y, x in clear_target: # BFS로 visited 한 대상들 한번에 변환
            arr[y][x] = "."

    return flag


def resetArr():
    for x in range(6):
        q = deque()
        for y in range(11, -1, -1): # 아래에서 부터, 뿌요가 있으면 기록
            if arr[y][x] != '.':
                q.append(arr[y][x])
        for y in range(11, -1, -1): # 뿌요 우선 기록하게 되면, 아래부터 쌓여 update 한 효과가 있음
            if q:
                arr[y][x] = q.popleft()
            else:
                arr[y][x] = '.'




dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

arr = []
for _ in range(12):
    arr.append(list(input()))
result = 0

while True:
    resetState = 0
    for y in range(12):
        for x in range(6):
            if arr[y][x] != '.':
                resetState += BFS(y, x, arr[y][x]) # 1그룹 처리가 끝나면 trigger

    if resetState == 0: # 모든 그룹 처리가 끝난 후 반영
        print(result)
        break
    else:
        result += 1
    resetArr() # 1턴이 종료되면 리셋
