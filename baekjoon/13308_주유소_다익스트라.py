# 1~N node, M개 간선, node별 주유단가, 간선 이동 km당 1리터 기름 사용
# 최소비용 계산

# [순서]
# - unit_list 작성
#   - *** 참고용
#   - 분리 구성
# - arr 작성 (왠만하면 memory와 분리 구성)
#   - 양방향
#   - unit_list[u] = (v, w)
# - memory 작성
#   - 상태 공간 배열 *****
#   - cnt in case by node 방식
#   - value ~ fuel_cost, idx ~ fuel_unit
# - Dijkstra
#   - visited x
#   - memory로 판단
#   - cost = w + unit * nw # ***** fuel 단가 * nw 이 포인트
#   - nnunit == node 의 단가와 nnode 의 단가 중 저가 선택. 이럴 경우 현재 node 이전의 가장 저렴한 unit을 불러올 수 있음


import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline

def Dijkstra(start):
    q = []
    memory[start][unit_list[start]] = 0
    heapq.heappush(q, (0, unit_list[start], start)) # node간 거리 최우선순위
    while q:
        w, unit, node = heapq.heappop(q)
        if node == N: # N 에 도달하면 w(누적 가중치) 출력
            return w
        if memory[node][unit] < w: # 이전에 거쳐가며 기록된 누적 fuel_cost < 현재 node의 누적 fuel_cost 이면 무시
            continue
        for nnode, nw in arr[node]:
            cost = w + unit * nw # ***** fuel 단가 * nw 이 포인트
            # 현재 총 비용이 다음 정점으로 가기 위해 드는 비용보다 작다면 우선순위 큐에 삽입
            if memory[nnode][unit] > cost:
                memory[nnode][unit] = cost
                heapq.heappush(q, (cost, min(unit_list[nnode], unit), nnode))  # node 의 단가와 nnode 의 단가 중 저가 선택. 이럴 경우 현재 node 이전의 가장 저렴한 unit을 불러올 수 있음


N, M = map(int, input().split())
unit_list = [-1] + list(map(int, input().split()))
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

# memory : 상태 공간 배열
memory = [[INF] * (max(unit_list) + 1) for _ in range(N + 1)]
print(Dijkstra(1))