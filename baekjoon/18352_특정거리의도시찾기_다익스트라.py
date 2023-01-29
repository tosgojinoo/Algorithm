# 다익스트라는 단방향, 양방향 둘다 가능
# 단방향, w 전부 1
# ***** 출발 == 도착 인 경우는 제외

import heapq
import sys
input = sys.stdin.readline

def Dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    visited = [INF] * (N+1)

    while heap:
        w, node = heapq.heappop(heap)

        if visited[node] < w:
            continue

        for nnode in arr[node]:
            cost = w + 1
            if visited[nnode] > cost:
                visited[nnode] = cost
                heapq.heappush(heap, (cost, nnode))

    return sorted([idx for idx, x in enumerate(visited) if x == K and idx != start])

N, M, K, X = map(int, input().split()) # N: node, M:edge, K:w_limit, X:start
INF = sys.maxsize
arr = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)

result = Dijkstra(X)
if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)

