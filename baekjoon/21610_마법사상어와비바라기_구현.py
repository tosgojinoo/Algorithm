def rain(dir, dis):
    moved_cloud = []
    for r, c in cloud: # 구름 있는 위치들
        nr = (r + dis*dx[dir]) % n # 격자의 양 끝단이 이어져 있는 형태
        nc = (c + dis*dy[dir]) % n
        arr[nr][nc] += 1 # 이동한 구름 위치에 물 추가
        visited[nr][nc] = 1 # 방문 처리
        moved_cloud.append((nr, nc))
    for r, c in moved_cloud:
        for i in range(1, 8, 2): # 대각선만 확인
            nr = r + dx[i]
            nc = c + dy[i]
            if 0<=nr<n and 0<=nc<n and arr[nr][nc]: # 범위내, 물 있을 경우
                arr[r][c] += 1 # 물 추가


n, m = map(int,input().split()) # 격자 N, 구름이동 M
arr = [list(map(int,input().split())) for _ in range(n)]
move_cloud = []

for i in range(m):
    d, s = map(int,input().split()) # 구름이 di 방향으로, si칸 이동
    move_cloud.append([d-1, s]) # d의 입력 idx는 1부터, shift -1 하여 계산은 0부터.
dx = [0, -1, -1, -1, 0, 1, 1, 1] # 9시 부터 시계방향
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)] # 구름 생성 위치. 입력 idx는 1부터, shift -1 하여 계산은 0부터.

for d in range(m):
    visited = [[0] * n for _ in range(n)]
    rain(move_cloud[d][0], move_cloud[d][1])
    cloud = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > 1: # 미방문, 2이상 칸에 구름 생성
                cloud.append((i, j)) # 구름 추가
                arr[i][j] -= 2 # 물 양 감소

print(sum(map(sum, arr)))