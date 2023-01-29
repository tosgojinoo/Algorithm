# 반례
# 출발 == 도착

# 주의
# case 2개: s > q > h > end, s > h > q > end


import sys
import heapq
input = sys.stdin.readline

def Dijkstra(start):
    visited = [INF] * (N+1)
    visited[start] = 0 # 이것을 추가하면, 나갔다가 자신에게 돌아오는 경우를 제외함
    heap = []
    heapq.heappush(heap, (0,start))

    while heap:
        w, node = heapq.heappop(heap)
        if visited[node] < w:
            continue

        for nnode, nw in arr[node]:
            cost = w + nw

            if visited[nnode] > cost:
                visited[nnode] = cost
                heapq.heappush(heap, (cost, nnode))

    return visited

T = int(input())
for tc in range(T):
    N, M, target_candid_num = map(int, input().split()) # node, edge, 목적지 후보 개수
    S, G, H = map(int, input().split()) # 출발, g-h 교차로 (g!=h, 발견한 곳)

    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, d = map(int, input().split())
        arr[a].append((b, d))
        arr[b].append((a, d))

    target_candid = []
    for _ in range(target_candid_num):
        target_candid.append(int(input()))

    INF = sys.maxsize
    route_S = Dijkstra(S) # s에서 각각의 노드까지의 최소 w 계싼
    route_G = Dijkstra(G)
    route_H = Dijkstra(H)
    ans = []
    # S -> G -> H -> target or S -> H -> G -> target == S -> target 확인
    # G-H(or H-G) 를 반드시 지나가는 경로가, S-target 의 최소경로와 일치하는지 확인
    for target in target_candid:
        if route_S[G] + route_G[H] + route_H[target] == route_S[target] or route_S[H] + route_H[G] + route_G[target] == route_S[target]:
            ans.append(target)
    ans.sort()
    for a in ans:
        print(a, end=' ')
    print()
