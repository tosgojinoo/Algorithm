# [키워드]
# 가중치, 방향, 최단경로 => 다익스트라 => 우선순위q heapq
# [순서]
# 출발 노드, 도착 노드, weight 설정
# 출발 노드 > 방문하지 않은 인접 노드 > 거리 계산 > 현재 거리보다 작으면 갱신
# 현재 노드에 인접한 모든 미방문 노드까지의 거리를 계산했다면, 현재 노드는 방문한 것이므로, 미방문 집합에서 제거한다.
# [종료]
# 도착 노드가 미방문 노드 집합에서 벗어남

# 다익스트라: 하나의 정점에서 모든 정점까지 최단거리
# 폴로이드-워셜: 모든 정점의 최단거리

# [순서]
# arr[node] = [(next_node, weight),...]
# visited, INF 로 초기화
# Dijkstra(start)
# - heapq.heappush(heap, (weight, node))
# - while q
# - heapq.heappop()
# - 현재 node에서 next_node로의 가중치 대비, 이미 방문해서 계산한 다른 방향으로의 cost가 작으면 visited 업데이트 안함
# - for 인접노드
#   - 현재까지의 cost + 인접노드로 가는 가중치 계산값이, 이미 방문해서 계산한 다른 방향으로의 cost보다 작으면 visited 업데이트
#   - heapq.heappush()

import heapq
import sys
input = sys.stdin.readline

# sys.setrecursionlimit(10**6)

def Dijkstra(start):
    # 시작 정점 가중치 0
    visited[start] = 0
    heapq.heappush(heap, (0, start)) # *** 순서 주의, 가중치가 앞

    while heap:
        cost, node = heapq.heappop(heap)

        # 이미 처리한 노드는 무시 (처리 했기 때문에, 노드의 원래 w > 누적 w)
        if visited[node] < cost:
            continue
        # 인접 노드 확인
        for nnode, nw in arr[node]:
            # 현재까지 가중치 w+ 다음노드까지 가중치 nw == 다음 노드까지의 누적 가중치
            ncost = cost + nw
            # 계산한 누적 가중치가 현재 기록된 값 보다 작으면 성립
            if ncost < visited[nnode]:
                visited[nnode] = ncost
                heapq.heappush(heap,(ncost, nnode))


INF = int(1e9)
V, E = map(int, input().split())
K = int(input()) # 시작점
visited = [INF]*(V+1)
heap = []
arr = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split()) # 출발 u, 도착 v, 가중치 w
    arr[u].append((v, w)) # (목적지, 가중치), 순서 무관
Dijkstra(K)
for i in range(1,V+1):
    print("INF" if visited[i] == INF else visited[i])
