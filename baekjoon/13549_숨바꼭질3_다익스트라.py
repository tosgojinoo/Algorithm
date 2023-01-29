# 1초 [x-1, x+1]
# 0초 [2*x]

# [주의]
# 종료 조건: heapq가 전부 사용되면 종료. node == K 아님(중간에 빠져나감)
# 출력: visited[K]. w 아님

# BFS 보다 오래 걸림

import heapq

def yield_iter(x):
    yield from [(x-1,1),(x+1,1),(x*2,0)]

def Dijkstra(start):
    heapq.heappush(heap, (0, start))

    visited[start] = 0

    while heap:
        w, node = heapq.heappop(heap)

        if w > visited[node]:
            continue

        for nnode, nw in yield_iter(node):
            cost = w + nw
            if 0<=nnode<=10**5 and visited[nnode] > cost:
                visited[nnode] = cost
                heapq.heappush(heap, (cost, nnode))

    print(visited[K])

N, K = map(int, input().split())

INF = 10**9
visited = [INF] * (10**5+1)
heap = []
Dijkstra(N)

