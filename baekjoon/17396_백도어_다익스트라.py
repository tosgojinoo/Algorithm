# N개의 분기점
# node 0 == 유섭이 현재 챔피언 위치
# node N-1 == 상대편 넥서스
# 나머지(1~N-2)는 중간 거점
# 적 챔피언, 와드, 미니언, 포탑 시야에 걸리면 못감
# 현 위치 ~ 넥서스까지 최소 시간 계산!

# [순서]
# - arr 구성
# - N-1을 제외한, 시야가 1인 모든 노드와 연결된 간선 정보 삭제 => check list 사용하여 제한
# - Dijkstra(1) 로 visited[N-1]계산


import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline

def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    visited = [INF] * (N)
    visited[start] = 0
    while q:
        w, node = heapq.heappop(q)
        if visited[node] < w:
            continue
        for nnode, nw in arr[node]:
            cost = w + nw
            if cost < visited[nnode] and check[nnode] == 0:
                visited[nnode] = cost
                heapq.heappush(q, (cost, nnode))
    return visited

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
check = list(map(int, input().split())) # 가지 못하는 곳
check[-1] = 0 # 넥서스는 제외
for _ in range(M):
    a, b, t = map(int, input().split())
    arr[a].append((b, t))
    arr[b].append((a, t))
visited = Dijkstra(0)
print(visited[N-1] if visited[N-1] < INF else -1)