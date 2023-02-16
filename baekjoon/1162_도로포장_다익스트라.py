'''
node 의 변경된 weight를 어떻게 반영해 줄 것인지 => memory로 관리. "w in case by node" 방식. 여기서는 case가 cnt(포장 횟수)
weight 변경 횟수 제한, 간선 적용 경우의 수를 어떻게 관리할 것인지 => Dijkstra에서 말미에 변경 횟수 제한. memory 관리

모든 node를 갈 필요 없이, 최소 비용(시간)으로 목표 지점까지의 이동이므로, Dijkstra, not kruskal
'''

import heapq, sys

def Dijkstra(start):
    queue = []
    cnt = 0
    memory[start][cnt] = 0
    heapq.heappush(queue, [0, start, cnt]) # weight, start node, cnt
    # or
    # queue = [[0, 1, 0]]
    # heapq.heapify(queue)

    while queue:
        cost, node, cnt = heapq.heappop(queue)

        if memory[node][cnt] < cost: # 더 작은 cost로 해당 node 까지 오는 case를 이미 확인함. 무시.
            continue

        for nnode, nweight in arr[node]:
            ncost = nweight + cost
            # 포장 안한 경우
            if memory[nnode][cnt] > ncost:
                memory[nnode][cnt] = ncost
                heapq.heappush(queue, [ncost, nnode, cnt])

            # 포장한 경우
            # elif로 안하고 if로 하는 이유는 모든곳을 돌아 도로포장을 했을때 가장 작은 값을 찾기 위함
            if cnt < K and memory[nnode][cnt + 1] > cost:
                memory[nnode][cnt + 1] = cost # nw == 0
                heapq.heappush(queue, [cost, nnode, cnt + 1]) # 포장했기 때문에 cnt+1


input = sys.stdin.readline
INF = sys.maxsize
N, M, K = map(int, input().split())

arr = [[] for _ in range(N + 1)]
memory = [[INF for _ in range(K + 1)] for _ in range(N + 1)]  # ***** 도로 포장 개수 확인. node 당 cnt index 에 w 저장. 동일 노드의 cnt 케이스별 가중치 관리
for i in range(M):
    x, y, weight = map(int, input().split())
    arr[x].append((y, weight)) # 무방향 그래프
    arr[y].append((x, weight))


Dijkstra(1)
print(min(memory[N]))