'''
[설명]
N×N
r행 c열에 있는 나라에는 A[r][c]명
인접한 나라 사이에는 국경선

- 인구 이동
    - 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속 -> while True: no_move break
        - 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하
            - 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
                - 인구 이동을 시작 -> 인접 이동 BFS
                - 연합
                - 연합을 이루고 있는 각 칸의 인구수
                    - (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
                    - 소수점 버림
        - 연합을 해체하고, 모든 국경선을 닫음

[문제]
인구 이동이 며칠 동안 발생
'''
'''
[알고리즘]
- BFS
    - people_result = moved_people // moved_cnt
    - for moved_country: people result
    - if moved_cnt > 1: is_moved = True
        
    
'''
'''
[구조]
- arr 저장
- dxy

- while True:
    - is_move = False
    - visited 
    - for 전체 탐색:
        - if 미방문:
            - BFS(i, j)

    - if is_move:
        - answer += 1
    - else:
        - break
- print(answer)


- BFS(x, y):
    - moved_people = arr[x][y] == 기준값
    - visited[x][y] = 방문 처리
    - moved_cnt = 1
    - moved_country = [(x, y)]

    - while queue:
        - for 4방:
            - if 범위 밖: 무시
            - if 기 방문: 무시
            - if 인구수 차이가 L~R 이내:
                - visited[nx][ny] = 방문처리
                - queue 추가 (nx, ny)
                - moved_people += arr[nx][ny]
                - moved_cnt ++
                - moved_country.append((nx, ny))

    - people_result = moved_people // moved_cnt

    - if moved_cnt > 1: # 1회 이상 움직였을 경우
        - is_move = True
        - for moved_country:
            - arr[x][y] = people_result
'''


from collections import deque

def BFS(x, y):
    global is_move
    moved_people = arr[x][y]
    moved_cnt = 1
    queue = deque([(x, y)])
    visited[x][y] = True
    moved_country = [(x, y)]

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not 0<=nx<n or not 0<=ny<n: # 범위 밖 무시
                continue

            if visited[nx][ny]: # 방문한 곳이면 무시
                continue

            if l <= abs(arr[x][y] - arr[nx][ny]) <= r: # L~R 범위 내면 계산
                visited[nx][ny] = True
                queue.append((nx, ny))
                moved_people += arr[nx][ny]
                moved_cnt += 1
                moved_country.append((nx, ny))

    people_result = moved_people // moved_cnt # 움직인 후 평균 인원 계산

    if moved_cnt > 1: # 1회 이상 움직였을 경우
        is_move = True
        for x, y in moved_country: # 움직인 모든 국가
            arr[x][y] = people_result

n, l, r = map(int, input().split()) # 크기, 범위 L ~ R
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0

while True:
    is_move = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n): # 전체 탐색
        for j in range(n):
            if not visited[i][j]:
                BFS(i, j)

    if is_move: # 움직임이 있었으면, 루프 지속
        answer += 1
    else:
        break

print(answer)