'''
[설명]
룰
1. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다. -> 리셋 함수(중력)
2. 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 -> BFS
연결된 같은 색 뿌요들이 한꺼번에 없어진다. -> 리셋 함수(폭발). 한 턴에 처리. -> BFS에 추가, resetState flag
이때 1연쇄가 시작된다. -> 연쇄 cnt
3. 뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면,
역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다. -> 리셋 함수(중력)
4. 아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, -> 리셋 함수(폭발) -> BFS에 추가
터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 증가
5. 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 -> 조건에 맞는 위치 저장 관리. 한 턴에 동시 처리 -> BFS에 추가, resetState flag
여러 그룹이 터지더라도 한번의 연쇄가 추가된다. -> 한 턴 표시 resetState flag

12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개 -> 12 x 6
.은 빈공간
.이 아닌것은 각각의 색깔의 뿌요
R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑
뿌요들이 전부 아래로 떨어진 뒤의 상태
뿌요 아래에 빈 칸이 있는 경우 없다

[문제]
현재 주어진 상황에서 몇 연쇄가 되는지 출력
하나도 터지지 않는다면 0을 출력
'''
'''
[알고리즘]
- BFS 전체 탐색 -> resetState 누적
- BFS
    - 탐색 queue, 제거 queue
    - 탐색 대상: 기준 value와 동일  
    - 제거 대상: 탐색 대상과 동일. 단, 소모하지 않고 보관.
    - cnt 4 이상일 경우만, 제거 대상 -> '.' 으로 변환.
- resetState
    - 1 이상 or 0만 갈림길
    - BFS 에서 누적 후 한번에 처리
    - 한 턴의 기준
    - 1 이상일 경우만, resetArr().
    - 0일 경우는, break. 
- resetArr
    - 열 순서로, 맨 아래 행부터 뿌요만 일단 다 저장한 후
    - 다시 맨 아래 행부터 뿌요를 기록
    - 제거 후 빈자리를 채우게 됨
'''
'''
[구조]
- while True:
    - 전체 탐색
        - if not '.'
            - resetState += BFS(y, x, arr[y][x])
    - if not resetState:
        result_combination 출력
        break
    - else:
        result_combination += 1
    - resetArr()
    
- BFS
    - 탐색 queue, 제거 queue, visited 선언
    - while 탐색 queue:
        - if 기준 value와 동일  
            - 탐색 queue, 제거 queue 추가
            - visited True
            - cnt += 1
    - if cnt >= 4:
        - flag True
        - 제거 대상 -> '.' 으로 변환
    
- resetArr
    - for 열
        - for 행 역순
            - 뿌요만 저장
        - for 행 역순
            - 뿌요만 기록
            - 뿌요 queue 모두 pop한 후, '.'(빈칸) 기록    
'''

from collections import deque

def BFS(y, x, value):
    queue = deque([(y, x)])
    clear_target = deque([(y, x)]) # clear_target

    visited = [[False] * 6 for _ in range(12)]
    visited[y][x] = True
    cnt = 1
    flag = 0

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not 0<=ny<=11 or not 0<=nx<=5:
                continue
            if arr[ny][nx] == value and not visited[ny][nx]:
                queue.append((ny, nx))
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
        queue = deque()
        for y in range(11, -1, -1): # 아래에서 부터, 뿌요가 있으면 기록
            if arr[y][x] != '.':
                queue.append(arr[y][x])
        for y in range(11, -1, -1): # 뿌요 우선 기록하게 되면, 아래부터 쌓여 update 한 효과가 있음
            if queue:
                arr[y][x] = queue.popleft()
            else:
                arr[y][x] = '.'


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

arr = []
for _ in range(12):
    arr.append(list(input())) # 12 x 6
result_combination = 0

while True:
    resetState = 0
    for y in range(12):
        for x in range(6):
            if arr[y][x] != '.':
                resetState += BFS(y, x, arr[y][x]) # 1그룹 처리가 끝나면 trigger

    if not resetState: # 모든 그룹 처리가 끝난 후 반영
        print(result_combination)
        break
    else:
        result_combination += 1
    resetArr() # 1턴이 종료되면 리셋
