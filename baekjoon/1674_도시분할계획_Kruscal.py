''' 
다익스트라 vs 크루스칼
- 공통점: 우선순위큐
- 차이점:
    - 다익스트라
        - heapq
        - DP
        - node 중심 (weight of node)
        - 출발점 지정
        - 일대다 최소 거리
        - 모든 정점 방문 optional
        - 최소: 임의의 두점간 최소 거리

    - 크루스칼
        - edge.sort()
        - union-find_parent
        - edge 중심 (weight of edge)
        - 간선 가중치 작은 것 부터 시작
        - 최소 신장 트리(MST)
        - 모든 정점 방문 required
        - 최소: 모든 정점 잇기 위한 최소 비용
'''
'''
두개 마을 & 최소 가중치 합
=> 모든 node에 대한 MST 구하고, 가장 마지막 weight edge 제거.
'''
import sys

input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a, b의 = find_parent(a), find_parent(b)
    parent[max(a, b)] = min(a, b)


N, M = map(int, input().split())

parent = [i for i in range(N + 1)] # 부모 저장

edges = [tuple(map(int, input().split())) for _ in range(M)] # a, b, weight
edges.sort(key=lambda x: x[2]) # 우선순위큐

ans = 0
end_v = 0 # 마지막 연결된 마을 연결 비용 저장
for edge in edges:
    a, b, weight = edge # 입력 순서 주의
    if find_parent(a) != find_parent(b):
        union(a, b)
        ans += weight
        end_v = weight # 마지막 연결된 마을의 연결 비용 저장

print(ans - end_v) # 마지막에 연결된 연결 비용 제거 후 출력