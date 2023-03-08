'''
[설명]
죄수 두 명을 탈옥
빈 공간은 '.'
지나갈 수 없는 벽은 '*'
문은 '#'
죄수의 위치는 '$'
상근이는 감옥 밖을 자유롭게 이동할 수 있고, -> padding
평면도에 표시된 죄수의 수는 항상 두 명 -> 죄수 위치 별로 저장 관리

[문제]
두 죄수를 탈옥시키기 위해서 열어야 하는 문의 최솟값 -> BFS, 죄수 위치 미리 저장.
'''
'''
[알고리즘]
- 외곽 자유롭게 이동 -> padding
- 시작 위치 없음 -> 죄수 위치 미리 저장 -> 두 죄수 위치를 시작점으로 지정 -> (0, 0)까지 이동
- 0-1 BFS
    - 가중치가 유리한 경우를 먼저 삽입(appenleft), 일반은 뒤에 삽입(append) 하는 BFS
    - 이 문제는, 문을 적게 여는 것이 유리하므로, 문이 아닐 경우 appendleft 
    - 최소 문 값 -> visited(init -1) + memory 기능(문 개수) 혼합
    - 문을 열지 않는 경우를 우선 처리
        - queue.appendleft([ny, nx])  
        - 가장 앞에 삽입
    - visited 를 리턴
- 문을 여는 케이스
    - visited(1): 1번 -> (0,0) 이동하며 여는 문 cnt를 visited에 저장
    - visited(2): 2번 -> (0,0) 이동하며 여는 문 cnt를 visited에 저장
    - visited(상근): (0,0) -> 1/2번 죄수로 이동하며 여는 문 cnt를 visited에 저장
    - arr 모든 영역 탐색하며, visited(1, 2, 상근)의 합이 최소가 되는 지점 확인
    - 이때, 벽이라면 제외, 문이라면 -2(3명중에 1명만 열면 되니 때문에 2인분 차감) 적용
'''
'''
[구조]
- arr 저장 -> padding
- 죄수 위치 저장
- BFS -> visited(1번 죄수)
- BFS -> visited(2번 죄수)
- BFS -> visited(상근)
- for y/x in arr:
    - if all visitied != -1:
        - if 벽: continue
        - if 문: visited 합에서 -2
        - min(ans)
'''

# BFS
#   - q.append([y,x,cnt])
#   - visited[문 on/off][y][x] -> *** state: 문 0/1/2 on
#   - prisons = 0
#   - if 문 on: cnt+=1
#   - ans = min(ans, cnt)
#   - if $:
#       - prisons += 1
#   - if prisons == 2:
#       print(cnt)


import sys
from collections import deque

def BFS(y, x):
    visited = [[-1] * (W + 2) for _ in range(H + 2)]  # padding. 열어야하는 문 개수 기록.
    queue = deque()
    queue.append([y, x])
    visited[y][x] = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny <= H + 1 and 0 <= nx <= W + 1: # 범위 내
                if visited[ny][nx] == -1: # 미방문
                    if arr[ny][nx] == '.' or arr[ny][nx] == '$':  # 문을 안열고 진행
                        visited[ny][nx] = visited[y][x]
                        queue.appendleft([ny, nx])  # 가장 앞에 삽입(우선 처리)
                    elif arr[ny][nx] == '#':  # 문을 여는 경우
                        visited[ny][nx] = visited[y][x] + 1 # 문 연 개수 추가
                        queue.append([ny, nx])
    return visited


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

tc = int(input())
for _ in range(tc):
    H, W = map(int, input().split()) # 높이 h와 너비 w. (2 ≤ h, w ≤ 100).
    arr = [list('.' * (W + 2))]  # 맨 윗줄 추가
    for i in range(H):
        arr.append(list('.' + input().strip() + '.'))
    arr.append(list('.' * (W + 2)))  # 맨 아랫줄 추가

    prisoner = []
    for i in range(H + 2):
        for j in range(W + 2):
            if arr[i][j] == '$': # 죄수위치 미리 저장
                prisoner.append([i, j])

    one = BFS(*prisoner[0]) # 첫번째 죄수 ~ (0,0) 까지 필요한 문 개수
    two = BFS(*prisoner[1]) # 두번째 죄수 ~ (0,0) 까지
    zero = BFS(0, 0) # (0,0) ~ 모든 곳 도착
    answer = sys.maxsize

    for y in range(H + 2):
        for x in range(W + 2):
            if one[y][x] != -1 and two[y][x] != -1 and zero[y][x] != -1: # 모든 경우에서 update 됐을 경우
                result = one[y][x] + two[y][x] + zero[y][x]  # 해당 위치에서 문을 여는 개수
                if arr[y][x] == '*':  # 벽은 제외
                    continue
                if arr[y][x] == '#':  # 한명만 열어도 되기 때문에 나머지 사람이 연 갯수인 2를 빼줌
                    result -= 2
                answer = min(answer, result)
    print(answer)