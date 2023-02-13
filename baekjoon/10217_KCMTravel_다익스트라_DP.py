'''
M원 이하, 가장 빠른 길
항상 최소 비용 이동이 아니므로, Dijkstra 적용 불가 => DP만 가능 -> X
"이전 고비용 + 이후 저비용" 이 정답이 될 수 있음
우선순위 중요! 지점이 우선될 수록 & 동일 지점 내 저비용
cost는 초기 설정값 적용 + memory 기능 + 수정 필요 => 따로 빼서 구성 필수! arr 를 절대 활용 불가, visited 추가 불가(초기값 모름)
'''

# KCM Travel

# import sys
from collections import deque
# input = sys.stdin.readline

MAX = 999999999999

def Dijkstra(arr, N, M):
    DP = [[MAX] * (M + 1) for _ in range(N)]
    DP[0][0] = 0

    queue = deque([(0, 0, 0)])  # dist, cost, node

    while queue:
        dist, cost, node = queue.popleft()
        if DP[node][cost] < dist:
            continue

        for nnode, ncost, ndist in arr[node]:
            new_dist = dist + ndist
            new_cost = cost + ncost
            if new_cost > M:
                continue  # 예산 초과
            if DP[nnode][new_cost] <= new_dist:
                continue  # 최소 거리 아님
            if DP[nnode][0] > new_dist:
                DP[nnode][0] = new_dist  # 최소값 저장
            for i in range(new_cost, M + 1):
                if DP[nnode][i] > new_dist:
                    DP[nnode][i] = new_dist
                else:
                    break

            queue.append((new_dist, new_cost, nnode))

    return DP[-1][0]


T = int(input())

for t in range(T):
    N, M, K = map(int, input().split())
    arr = [[] for _ in range(N)]
    for _ in range(K):
        u, v, c, d = map(int, input().split()) # 출발, 도착, 비용, 소요시간
        arr[u - 1].append((v - 1, c, d))

    result = Dijkstra(arr, N, M)
    if result == MAX:
        print('Poor KCM')
    else:
        print(result)