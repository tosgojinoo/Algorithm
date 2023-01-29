# [중요]
# node 의 변경된 weight를 어떻게 반영해 줄 것인지 => memory로 관리. "w in case by node" 방식. 여기서는 case가 cnt(포장 횟수)
# weight 변경 횟수 제한, 간선 적용 경우의 수를 어떻게 관리할 것인지 => Dijkstra에서 말미에 변경 횟수 제한. memory 관리

import heapq, sys

def Dijkstra(start):
    q = []
    cnt = 0
    memory[start][cnt] = 0
    heapq.heappush(q, (0, start, cnt)) # w, node, cnt

    while q:
        w, node, cnt = heapq.heappop(q)

        if memory[node][cnt] < w:
            continue

        for nnode, nw in arr[node]:
            cost = nw + w
            # 포장 안한 경우
            if memory[nnode][cnt] > cost:
                memory[nnode][cnt] = cost
                heapq.heappush(q, (cost, nnode, cnt))

            # 포장한 경우
            # elif로 안하고 if로 하는 이유는 모든곳을 돌아 도로포장을 했을때 가장 작은 값을 찾기 위함
            if cnt < K and memory[nnode][cnt + 1] > w:
                memory[nnode][cnt + 1] = w # nw == 0
                heapq.heappush(q, (w, nnode, cnt + 1)) # 포장했기 때문에 cnt+1


input = sys.stdin.readline
INF = sys.maxsize
N, M, K = map(int, input().split())

arr = [[] for _ in range(N + 1)]
memory = [[INF for _ in range(K + 1)] for _ in range(N + 1)]  # ***** 도로 포장 개수 확인. node 당 cnt index 에 w 저장. 동일 노드의 cnt 케이스별 가중치 관리
for i in range(M):
    x, y, z = map(int, input().split())
    arr[x].append((y, z)) # 무방향 그래프
    arr[y].append((x, z))


Dijkstra(1)
print(min(memory[N]))