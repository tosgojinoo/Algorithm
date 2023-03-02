from collections import deque

def rotate(order):
    global arr
    if not order: # order == 0
        return
    s = 2 ** order
    arr_new = [[0] * N for _ in range(N)] 
    for i in range(0, N, s):
        for j in range(0, N, s):
            for x in range(s):
                for y in range(s):
                    arr_new[i + x][j + y] = arr[i + s - y - 1][j + x] # 수식 중요.
    arr = arr_new
    return

def melt():
    global arr
    arr_copy = [i[:] for i in arr]
    for x in range(N):
        for y in range(N):
            cnt = 0 # 주위 얼음수
            if arr[x][y]: # 얼음 있으면.
                for d in range(4): # 4방 확인
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N: # 범주 내면
                        if arr[nx][ny]: # 얼음 있으면
                            cnt += 1
                if cnt < 3: # 주위 얼음수 3 미만이면.
                    arr_copy[x][y] -= 1 # 차감
    arr = arr_copy
    return


def BFS(): # 가장 큰 덩어리 칸의 개수 구하기
    MAX = 0
    visited = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and arr[x][y]:
                visited[x][y] = True
                queue = deque([(x, y)])
                cnt = 1
                while queue: # 한 덩어리 내 얼음칸 cnt
                    x, y = queue.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and arr[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                cnt += 1

                MAX = max(MAX, cnt)
    return MAX

n, m = map(int, input().split())
N = 2 ** n
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(m):
    rotate(order[i])
    melt()

print(sum(map(sum, zip(*arr))))
print(BFS())