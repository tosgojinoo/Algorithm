import sys
input = sys.stdin.readline

def find_parent(node):
    if node != parent[node]:
        parent[node] = find_parent(parent[node])
    return parent[node]
def union(node1, node2):
    root1 = find_parent(node1)
    root2 = find_parent(node2)
    # 여기서는 rank 고려 없이 작은 수를 무조건 부모 노드로 설정
    parent[root2] = root1

n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(m)]
# 원래 kruskal은 가중치 작읕 것부터 오름차순으로 연결하지만, 여기서는 반대.
arr = sorted(arr, key=lambda x: x[2], reverse=True)
start, end = map(int, input().split())
parent = list(range(n+1))

# 가중치 큰 것에서부터 내림차순으로 연결.
# start -> end가 연결되면, weight 출력 후 정지.
# 자연스럽게 최대 가능 weight 확인.
for node1, node2, weight in arr:
    union(node1, node2)
    if find_parent(start) == find_parent(end):
        print(weight)
        break