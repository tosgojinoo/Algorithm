from collections import deque

def BFS():
    queue = deque([(0, 0)]) # x, y
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = 1
                # 공기만 탐색, 치즈는 탐색 없이 저장만 하면 내부 공간은 접할 수 없음
                if arr[nx][ny] == 0: # 공기면 계속 탐색하기 위해 큐에 넣음
                    queue.append((nx, ny))
                elif arr[nx][ny] == 1: # 치즈면 한 번에 녹이기 위해 melt에 넣음
                    melt.append((nx, ny))

    for x, y in melt:
        arr[x][y] = 0  # 공기와 닿은 치즈를 한 번에 녹임
    return len(melt)  # 녹인 치즈 갯수 리턴


N, M = map(int, input().split())
arr = []
totalCheeze = 0
for i in range(N):
    arr.append(list(map(int, input().split())))
    totalCheeze += sum(arr[i])  # 전체 치즈 갯수 카운트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    visited = [[0] * M for _ in range(N)]
    melt = []
    meltCnt = BFS()
    totalCheeze -= meltCnt
    if totalCheeze == 0:  # 치즈를 다 녹였으면
        print(time, meltCnt, sep='\n')  # 시간과 직전에 녹인 치즈 갯수를 출력
        break
    time += 1