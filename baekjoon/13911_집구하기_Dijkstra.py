import heapq
import sys
input = sys.stdin.readline

INF = 987654321

def Dijkstra(queue, distance):
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for nxt, cost in arr[now]:
            value = cost + dist
            if distance[nxt] > value:
                distance[nxt] = value
                heapq.heappush(queue, (value, nxt))


V, E = map(int, input().split())
arr = [[] for _ in range(V + 1)]
distance_mc = [INF] * (V + 1)
distance_star = [INF] * (V + 1)
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

mcs, mc_limit = map(int, input().split())
mc_nodes = list(map(int, input().split()))
stars, star_limit = map(int, input().split())
star_nodes = list(map(int, input().split()))
mqueue, squeue = [], []

for mc in mc_nodes:
    heapq.heappush(mqueue, (0, mc)) # mc 들을 잇는 가상 최정점 mc
    distance_mc[mc] = 0

for star in star_nodes:
    heapq.heappush(squeue, (0, star)) # star 들을 잇는 가상 최정점 star
    distance_star[star] = 0
answer = INF
Dijkstra(mqueue, distance_mc)
Dijkstra(squeue, distance_star)
for i in range(1, V + 1):
    if distance_mc[i] <= 0 or distance_mc[i] > mc_limit: # 가상 최정점과 edge(거리 0) or 제한 거리보다 큰 경우 제외
        continue
    if distance_star[i] <= 0 or distance_star[i] > star_limit:
        continue
    answer = min(answer, distance_mc[i] + distance_star[i])
print(answer if answer < INF else -1)