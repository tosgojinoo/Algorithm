# BFS & Priority Queue
# max heap 형태로 사용하려면(python heapq는 기본적으로 min heaq)
# 1) (우선순위, 값) 형태의 tuple로 저장
# 2) '우선순위'를 마이너스로 구성하여, max heap 구현 (원래 값은 클수록 작아지며, 우선순위 높아짐)

# 중복하여 같은 길을 지날 때는 더이상 탐색하지 않고 횟수만 늘려주어 전체적인 시간 복잡도를 낮춤

from heapq import heappush, heappop, heapify

def BFS_PQ():
    global visited
    q = []
    heapify(q)
    heappush(q, (-arr[0][0], 0, 0))
    visited[0][0] = 1

    while q:
        now, y, x = heappop(q) #
        if y==M-1 and x==N-1:
            continue
        for dy, dx in moves:
            ny, nx = y+dy, x+dx
            if 0<=ny<M and 0<=nx<N:
                if arr[ny][nx] < -now:
                    if visited[ny][nx] == 0: # 처음 방문할 경우만 heap에 추가
                        heappush(q, (-arr[ny][nx], ny, nx))
                    visited[ny][nx] += visited[y][x] # 이전에 방문했을 경우, 값만 추가
    return


# 세로의 크기 M과 가로의 크기 N
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
moves = [(1,0), (-1,0), (0,1), (0,-1)]
visited = [[0]*N for _ in range(M)]
BFS_PQ()
print(visited[M-1][N-1])