'''
가장 적은 비용으로 모든 노드를 연결
최소 비용 신장 트리(Minimum Spanning Tree)
간선을 거리가 짧은 순서대로 그래프에 포함
모든 노드들을 최대한 적은 비용으로 '연결'
모든 간선 정보를 오름차순으로 정렬한 뒤에 비용이 적은 간선부터 그래프에 포함
주의: no "사이클". 노드가 같은 최상위 정점을 갖는지 확인
1. 정렬된 순서에 맞게 노드를 그래프에 포함시킨다.
2. 포함시키기 전에는 사이클 테이블을 확인한다.
3. 사이클을 형성하는 경우 간선을 포함하지 않는다.
'''


def make_set(vertice): # 부모 참조 table 초기화
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice): # 해당 vertice의 최상위 정점 찾기
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2): # 두 정점 연결
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal():
    minimum_spanning_tree = []

    # 초기화
    for vertice in arr['vertices']:
        make_set(vertice)

    # 간선 weight 기반 sorting
    edges = arr['edges']
    edges.sort()

    # 간선 연결 (사이클 없게)
    for edge in edges:
        weight, vertice1, vertice2 = edge
        # 부모가 같을 때 union 하면 싸이클 발생. 싸이클 미 발생시(부모가 다름), 집합에 포함
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.append(edge)

    return minimum_spanning_tree

arr = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()
print(kruskal())
print(rank)
print(parent)
