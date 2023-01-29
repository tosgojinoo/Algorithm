# 1~N node, M개 간선, 양방향, node 1 출발
# 여우는 일정 속도, 늑대는 빠르지만 체력 부족
# 늑대는 2배 + 절반 속도 반복
# 여우가 늑대보다 먼저 도착할 수 있는 node 몇개인지?

# [순서]
# [main]
# arr 구성
#   - arr[u].append((v, w))
#   - *** w 에 2배 해주는 이유 -> 늑대를 절반 속도로 적용할 때 //2 에서 나머지 미생성
# Dijkstra_여우(1) 계산
# Dijkstra_늑대(1) 계산
# Dijkstra_여우(1) - Dijkstra_늑대(1), 양수인 index 개수 카운팅
# [Dijkstra_여우]
#   - Dijkstra 기본 구성
# [Dijkstra_늑대]
#   - status 변수 추가 ***
#       - 홀수/짝수번째 node 구분 기능, 홀수번째는 nw*2, 짝수번째는 nw/2, 적용
#       - status 변수 True/False로 구분
#   - visited
#       - 상태 공간 배열
#       - "w in case by node"
#       - idx(case): status / value: cost
#   - heap: 가중치 우선 정렬

# Dijkstra 에서, visited는 방문 여부 + 누적 w 저장


import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def Dik_fox(start):
    visited = [INF for _ in range(N+1)]
    visited[start] = 0
    q = []
    heapq.heappush(q, (visited[start], start)) # 가중치 우선 정렬

    while q:
        w, node = heapq.heappop(q)
        if visited[node] < w:
            continue
        for nw, nnode in arr[node]:
            cost = w + nw
            if visited[nnode] > cost:
                visited[nnode] = cost
                heapq.heappush(q, (visited[nnode], nnode))
    return visited

def Dik_wolf(start):
    # visited[0] 빠르게 도착 / visited[1] 느리게 도착
    visited = [[INF] * (N+1) for _ in range(2)]
    visited[1][start] = 0
    status = False
    q = []
    heapq.heappush(q, (visited[1][start], start, status))

    while q:
        w, node, status = heapq.heappop(q)
        if status and visited[0][node] < w:
            continue
        elif not status and visited[1][node] < w:
            continue

        for nw, nnode in arr[node]:
            if status:  # 빠르게 도착했다면, 느리게 출발
                cost = w + (nw * 2)
                if visited[1][nnode] > cost:
                    visited[1][nnode] = cost
                    heapq.heappush(q, (visited[1][nnode], nnode, False)) # status -> False
            else:  # 느리게 도착했다면, 빠르게 출발
                cost = w + (nw // 2)
                if visited[0][nnode] > cost:
                    visited[0][nnode] = cost
                    heapq.heappush(q, (visited[0][nnode], nnode, True)) # status -> Ture

    return visited


N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    arr[a].append((d * 2, b)) # *** w 에 2배 해주는 이유 -> 늑대를 절반 속도로 적용할 때 //2 에서 나머지 미생성
    arr[b].append((d * 2, a))

fox = Dik_fox(1)
print(fox)
wolf = Dik_wolf(1)
print(wolf)

answer = 0
for i in range(1, N+1):
    if fox[i] < min(wolf[0][i], wolf[1][i]):
        answer += 1
print(answer)




'''TC
5 6
1 2 3
1 3 2
2 3 2
2 4 4
3 5 4
4 5 3

1
--

5 4
1 2 1
2 3 1
3 4 1
4 5 1

2
--

5 5
1 2 1
2 3 1
3 4 1
4 5 2
1 4 3

2
--

5 5
1 2 1
1 4 1
4 5 1
5 1 1
2 3 100

0
--
'''