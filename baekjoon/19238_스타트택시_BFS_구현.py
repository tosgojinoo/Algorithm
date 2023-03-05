import sys
from heapq import heappop, heappush

input_list = lambda dtype=int: [dtype(i) for i in sys.stdin.readline().strip().split()]


def BFS(start_point, target_func):
    queue = [(0, *start_point)]
    visited = [[False] * (N + 2) for _ in range(N + 2)]
    visited[start_point[0]][start_point[1]] = True

    while queue:
        dist, i, j = heappop(queue)
        if target_func(i, j): # 가장 가까운 지점 도착시 종료(1> 가장 가까운 고객, 2> 고객 도착점까지의 가장 가까운 dist)
            return i, j, dist

        for ni, nj in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
            if not visited[ni][nj] and arr[ni][nj] != 1: # 미방문 & 벽이 아니면.
                visited[ni][nj] = True
                heappush(queue, (dist + 1, ni, nj))

    return 0, 0, F + 1 # i, j, dist. dist > F 이므로, 종료 활성화.



N, M, F = map(int, input().split()) # arr 크기, 초기 연료량 F.
arr = [[1] * (N + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1] * (N + 2)] # 가장자리를 1로 padding. 1 은 벽.
T = list(map(int, input().split())) # 운전 시작하는 칸의 행, 열 번호
passenger = {}

for _ in range(M):
    start_i, start_j, end_i, end_j = map(int, input().split()) # 승객의 출발지 행과 열 번호, 목적지 행과 열 번호
    passenger[(start_i, start_j)] = (end_i, end_j)
    arr[start_i][start_j] = 2 # 승객 출발지 2로 표기

stop_flag = 0
for _ in range(M):
    start_i, start_j, dist = BFS(T, lambda i, j: arr[i][j] == 2) # 운전자 출발지 ~ 가장 가까운 고객까지 이동
    if dist > F:
        stop_flag = -1
        break
    F -= dist # 이동 거리만큼 연료 감소
    arr[start_i][start_j] = 0 # 고객 시작 위치 초기화

    end_i, end_j, dist = BFS((start_i, start_j), lambda i, j: (i, j) == passenger[(start_i, start_j)]) # 고객 출발지 ~ 고객 도착지까지 가장 가까운 dist 계산
    if dist > F:
        stop_flag = -1
        break
    T = (end_i, end_j)
    F += dist

print(stop_flag if stop_flag == -1 else F)