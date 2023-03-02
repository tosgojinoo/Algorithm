from collections import deque

def BFS(x, y, visited):
    global is_move
    moved_people = arr[x][y]
    count = 1
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
                count += 1
                moved_country.append((nx, ny))

    people_result = moved_people // count # 움직인 후 평균 인원 계산

    if count > 1: # 1회 이상 움직였을 경우
        is_move = True
        for x, y in moved_country: # 움직인 모든 국가
            arr[x][y] = people_result

n, l, r = map(int, input().split(' ')) # 크기, 범위 L ~ R
arr = [list(map(int, input().split(' '))) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

is_move = False
answer = 0

while True:
    is_move = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n): # 전체 탐색
        for j in range(n):
            if not visited[i][j]:
                BFS(i, j, visited)

    if is_move: # 움직임이 있었으면, 루프 지속
        answer += 1
    else:
        break

print(answer)