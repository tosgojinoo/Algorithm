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

def Dijkstra():
    DP = [[MAX] * (M + 1) for _ in range(N)]
    DP[0][0] = 0

    queue = deque([(0, 0, 0)])  # dist, cost, node

    while queue:
        dist, cost, node = queue.popleft()
        if DP[node][cost] < dist:
            continue

        for nnode, ncost, ndist in arr[node]:
            cum_dist = dist + ndist
            cum_cost = cost + ncost
            if cum_cost > M:
                continue  # 예산 초과
            if DP[nnode][cum_cost] <= cum_dist:
                continue  # 최소 거리 아님

            DP[nnode][0] = min(DP[nnode][0], cum_dist)

            # 동일 지점 내 다른 금액에 대해 지점의 최소거리로 update
            for cum_cost_add in range(cum_cost, M + 1):
                if DP[nnode][cum_cost_add] > cum_dist:
                    DP[nnode][cum_cost_add] = cum_dist
                else:
                    break

            queue.append((cum_dist, cum_cost, nnode))

    return DP[-1][0]


T = int(input())

for t in range(T):
    N, M, K = map(int, input().split())
    arr = [[] for _ in range(N)]
    for _ in range(K):
        u, v, c, d = map(int, input().split()) # 출발, 도착, 비용, 소요시간
        arr[u - 1].append((v - 1, c, d))

    result = Dijkstra()
    if result == MAX:
        print('Poor KCM')
    else:
        print(result)