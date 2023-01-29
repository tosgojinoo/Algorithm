# 방향성 없는 그래프
# 최단거리 이동
# 주어진 두 정점 통과
# 반복 이동, 도착 가능

# 1 > V1 > V2 > N 이동
# - 1 > V1 최단, V1 > V2 최단, V2 > N 최단

# 가중치가 나오면, arr & visited

import heapq
import sys

input = sys.stdin.readline

def Dijkstra(start, end):
    heap = []
    visited = [INF] * (N + 1)
    visited[start] = 0
    heapq.heappush(heap, (0, start)) # w, node 를 변수로 넣어야 함 / w_start 는 무조건 0

    while heap:
        w, node = heapq.heappop(heap) # idx -> node 직접 가는 w

        if visited[node] < w: # visited[node]: node 까지 돌아서 가는 w
            continue

        for nnode, nw in arr[node]:
            cost = visited[node] + nw # 돌아서
            if visited[nnode] > cost:
                visited[nnode] = cost
                heapq.heappush(heap, (cost, nnode))

    return visited[end] # *** 전부 계산 후 end 의 누적 cost 만 출력

N, K = map(int, input().split())
INF = sys.maxsize
arr = [[] for _ in range(N+1)]
for _ in range(K):
    u, v, w = map(int, input().split())
    # 무방향 그래프, 양쪽 저장
    arr[u].append((v, w))
    arr[v].append((u, w))
V1, V2 = map(int, input().split())

# ***** V1, V2를 포함하는 최단 경로는 두가지 경우의 수
route1 = Dijkstra(1, V1) + Dijkstra(V1, V2) + Dijkstra(V2, N)
route2 = Dijkstra(1, V2) + Dijkstra(V2, V1) + Dijkstra(V1, N)

result = min(route1, route2)
print(result if result < INF else -1) # result 가 INF 보다 클 수도 있음. 범위로 제한하기.
