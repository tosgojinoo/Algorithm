'''
[설명]
모든 섬을 다리로 연결
N×M
격자의 각 칸은 땅이거나 바다
섬은 연결된 땅이 상하좌우로 붙어있는 덩어리
색칠되어있는 칸은
다리는 바다에만 건설
다리의 길이는 다리가 격자에서 차지하는 칸의 수
다리를 연결해서 모든 섬을 연결
섬 A에서 다리를 통해 섬 B로 갈 수 있을 때, 섬 A와 B를 연결
다리의 양 끝은 섬과 인접한 바다 위
한 다리의 방향이 중간에 바뀌면 안됨
다리의 길이는 2 이상
다리의 방향은 가로 또는 세로
방향이 가로인 다리는 다리의 양 끝이 가로 방향으로 섬과 인접
방향이 세로인 다리는 다리의 양 끝이 세로 방향으로 섬과 인접

섬 A와 B를 연결하는 다리가 중간에 섬 C와 인접한 바다를 지나가는 경우에 섬 C는 A, B와 연결되어 있는 것이 아님
0은 바다, 1은 땅을 의미

[문제]
모든 섬을 연결하는 다리 길이의 최솟값
모든 섬을 연결하는 것이 불가능하면 -1
'''
'''
[알고리즘]
- memory
    - country_coord
        - [(y,x,country_idx)]
        - 바다 제외, 육지(섬)의 모든 좌표에 대해 저장
        - distance 계산시, 바다와 인접한 곳만 활용하게 됨 
        - DFS 로 구성
    
- DFS > 섬 넘버링 > distance(weight) 계산 > kruskal > MST 간선수 충분 확인
'''
'''
[구조]
- arr 저장
- visited 설정
- country_coord = [(y,x,country_idx)]

- for 전체 탐색
    - if 미방문 & 섬 발견:
        - country_idx ++
        - DFS(y, x, country_idx)

# kruskal
- parent = country 개수만큼 생성
- edges = []
- distance()
- edges.sort()
- for edges:
    - if find_parent(a) != find_parent(b):
        - union(a, b)
        - result += weight
        - cnt += 1

- if MST에서 필요 간선수는 len(node)-1
    - print(result)
- else:
    - print(-1)


- DFS(y, x, country_idx):
    - if 범위밖: return
    - if 미방문 & 섬:
        - visited[y][x] = country_idx로 방문 표기
        - country_coord.append((y, x, country_idx))
        - for 4방향: 
            - DFS(ny, nx, country_idx)
    - return

- distance():
    - for country_coord: (y,x,country_idx)
        - for 4방향:
            - dist = 초기화

            - while True:
                - if 범위밖: break
                - else:
                    - if 섬 내부: break
                    - if 바다(미방문): 
                        - dist ++
                        - continue
                    - if 거리가 2 이하: break

                    - edges 추가 (dist, country_idx, visited[ny][nx]) 거리를 weight
                    - break

- find_parent(x):
- union(a, b):

'''

import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(y, x, country_idx):
    if not (0<=y<N) or not (0<=x<M):
        return
    if not visited[y][x] and arr[y][x]:
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
                    if not visited[ny][nx]: # 바다(미방문)
                        ny, nx = ny + dy[d], nx + dx[d]
                        dist += 1
                        continue
                    if dist < 2: # 거리가 2 이하면 무시
                        break

                    edges.append((dist, country_idx, visited[ny][nx])) # 거리를 weight
                    break

def find_parent(node):
    if node != parent[node]:
        parent[node] = find_parent(parent[node])
    return parent[node]
def union(node1, node2):
    root1 = find_parent(node1)
    root2 = find_parent(node2)
    # 여기서는 rank 고려 없이 작은 수를 무조건 부모 노드로 설정
    parent[max(root1, root2)] = min(root1, root2)

N, M = map(int, input().split()) # 세로 크기 N과 가로 크기 M
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
country_idx = 0
country_coord = [] # (y,x,country_idx)
edges = []
result = 0

for y in range(N):
    for x in range(M):
        if not visited[y][x] and arr[y][x]: # 섬 발견시
            country_idx += 1 # country idx. 1부터 시작.
            DFS(y, x, country_idx)

parent = [i for i in range(country_idx+1)] # 0 포함 country 개수만큼 생성

distance()
edges.sort()
cnt = 0

for edge in edges:
    weight, node1, node2 = edge

    if find_parent(node1) != find_parent(node2):
        union(node1, node2)
        result += weight
        cnt += 1

if cnt == country_idx - 1: # MST에서 필요 간선수는 len(node)-1
    print(result)
else:
    print(-1)