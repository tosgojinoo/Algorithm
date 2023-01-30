def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index
def dijkstra(start):
    # 시작노드 -> 시작노드 거리 계산 및 방문 처리
    distance[start] = 0 # 시작 노드는 0으로 초기화
    visited[start] = True

    # 시작노드의 인접한 노드들에 대해 최단거리 계산
    for adj_start in graph[start]:
        distance[adj_start[0]] = adj_start[1] # 시작 노드와 연결된 노드들의 거리 입력

    # 시작노드 제외한 n-1개의 다른 노드들 처리
    for _ in range(n-1):
        now = get_smallest_node() # 방문 x, 거리가 구해진 노드 중 가장 짧은 거리인 것을 선택
        visited[now] = True # 방문 처리

        # 해당노드의 인접한 노드들 간의 거리 계산
        for adj_now in graph[now]:
            if distance[now] + adj_now[1] < distance[adj_now[0]]: # 기존에 입력된 값보다 더 작은 거리가 나온다면,
                distance[adj_now[0]]= distance[now] + adj_now[1]    # 값을 갱신한다.

n, m = map(int, input().split())
start = int(input())                                                                 # 시작할 노드
INF = 1e9

graph = [[] for _ in range(n+1)] # 1번 노드부터 시작하므로 하나더 추가
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split()) # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치
    graph[u].append((v, w)) # 거리 정보와 도착노드를 같이 입력합니다.

dijkstra(start)
print(distance)