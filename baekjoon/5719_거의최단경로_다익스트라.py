# 최단 경로는 답에서 제외
# 최단 경로에 포함된 경로를 제외한 도로 중 가장 짧은 것
# 최단 경로가 복수개일 경우, 각각의 최단 경로에 해당하는 간선을 우선 다 제거한 후에 차선 경로 찾아야 함

# ***** 순서
# - 정방향 arr(타겟팅 삭제를 위해 dict), 역방향 r_arr 저장
# - 다익스트라 로 최단 경로 cost 계산, visited에 cost 저장
# - BFS 로 역추적
#   - D 시작, S 종료(break 아니고, continue 처리하여 모든 경우를 확인)
#   - D에서 하나 이전 노드로 옮겨가며, 역계산된 w + 이전 node까지의 누적 cost == 현재 node 누적 cost 경우 제거 대상으로 포함
# - 최단 경로 포함된 간선(제거 대상) 모두 삭제
# - 다익스스타로 수정된 최단 경로 cost 계산

import sys, heapq
from collections import deque
input = sys.stdin.readline

def Dijkstra(start):
    global visited
    heap = []
    heapq.heappush(heap, (0, start))
    visited[start] = 0

    while heap:
        w, node = heapq.heappop(heap)

        if visited[node] < w:
            continue

        # items 로 넣지 말 것, dict가 없을 수 도 있음
        for nnode in arr[node]:
            cost = w + arr[node][nnode]
            if visited[nnode] > cost:
                visited[nnode] = cost
                heapq.heappush(heap, (cost, nnode))


def BFS():
    global visited, rm_list
    q = deque()
    q.append(D)

    while q:
        node = q.popleft()

        if node == S:
            continue

        for rnode, rw in r_arr[node]:
            if rw + visited[rnode] == visited[node]:
                # list + if 처리해야 메모리/시간 제한 회피. set 처리할 경우 문제됨.
                if (rnode, node) not in rm_list:
                    rm_list.append((rnode, node))
                    q.append(rnode)

'''
def Dijkstra(start):
    visited = [(INF, set([]))] * N
    visited[start] = (0, set([start]))
    heap = []
    route = deque([start])
    heapq.heappush(heap, (0, start, route))

    while heap:
        w, node, route = heapq.heappop(heap)

        if visited[node][0] < w:
            continue

        for nnode, nw in arr[node]:
            cost = w + nw
            if visited[nnode][0] > cost:
                route.append(nnode)
                tmp = route.copy()
                visited[nnode] = (cost, tmp)
                heapq.heappush(heap, (cost, nnode, tmp))
                route.pop()

    return visited
'''

while True:
    N, M = map(int, input().split())
    if N==0 and M==0:
        break
    S, D = map(int, input().split())
    arr = [dict() for _ in range(N)]
    r_arr = [[] for _ in range(N)]
    for _ in range(M):
        u, v, p = map(int, input().split())
        arr[u][v] = p
        r_arr[v].append((u, p))

    INF = sys.maxsize
    # print(arr)
    # print(r_arr)
    # 최소 경로 cost 계산
    visited = [INF] * N
    Dijkstra(S)
    # 최소 경로의 경우의 수 계산, 종점에서 시작
    # print(visited)
    # 삭제 대상 간선을 계산하면서, 반복 입력 될 수 있으므로, set 처리
    rm_list = []
    BFS()
    # print(rm_list)
    # 최단경로에 포함되는 간선 모두 삭제, dict 이므로 바로 삭제 가능
    for rnode, node in rm_list:
        del arr[rnode][node]
    # print(arr)
    # 재계산
    visited = [INF] * N
    Dijkstra(S)
    ans = visited[D]
    print(ans if ans < INF else -1)
