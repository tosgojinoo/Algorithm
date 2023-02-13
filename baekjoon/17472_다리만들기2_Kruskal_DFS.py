''' my idea
다리 개수 경우의 수??
다리로 연결하면 linked list 구성
다리 연경이 끝나면 백트래킹으로 모든 node 갈 수 있는지 확인
가능하면 result 추가
'''
'''
1) DFS, BFS로 나라 index 선정, 좌표 값 저장.
2) 저장한 좌표와 나라 index 기반 나라 간 거리 계산. 구한 거리를 비용으로 생각하는 간선 설정.
3) 구한 거리를 정렬. 최소 신장 트리를 기반으로 크루스칼 혹은 프림 알고리즘을 적용.
'''
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(y, x, country_idx):
    if not (0<=y<N) or not (0<=x<M):
        return
    if visited[y][x] == 0 and arr[y][x]:
        visited[y][x] = country_idx # country 만 visited. 바다는 x.
        country_coord.append((y, x, country_idx))
        for d in range(4): # 4방향
            ny, nx = y+dy[d], x+dx[d]
            DFS(ny, nx, country_idx)
    return

def distance():
    for coord in country_coord:
        y, x, country_idx = coord
        for d in range(4):
            dist = 0
            ny, nx = y + dy[d], x + dx[d]

            while True:
                if not (0<=ny<N) or not (0<=nx<M):
                    break
                else:
                    if country_idx == visited[ny][nx]: # 섬 내부면 무시
                        break
                    if visited[ny][nx] == 0: # 바다면 전진
                        ny, nx = ny + dy[d], nx + dx[d]
                        dist += 1
                        continue
                    if dist < 2: # 거리가 2 이하면 무시
                        break

                    edges.append((dist, country_idx, visited[ny][nx])) # 거리를 weight
                    break

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a, b = find_parent(a), find_parent(b)
    parent[max(a, b)] = min(a, b)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
visited = [[0] * M for i in range(N)]
country_idx = 0
country_coord = [] # (y,x,country_idx)
edges = []
result = 0

for y in range(N):
    for x in range(M):
        if not visited[y][x] and arr[y][x] == 1: # 섬 발견시
            country_idx += 1 # country idx. 1부터 시작.
            DFS(y, x, country_idx)

parent = [i for i in range(country_idx+1)] # 0 을 제외한 country 개수만큼 생성

distance()
edges.sort()
cnt = 0
print(edges)
for edge in edges:
    weight, a, b = edge

    if find_parent(a) != find_parent(b): # 최상위 부모
        union(a, b)
        result += weight
        cnt += 1

if cnt == country_idx - 1: # MST에서 필요 간선수는 len(node)-1
    print(result)
else:
    print(-1)