import sys
input = sys.stdin.readline

def find_parent(node):
    if node != parent[node]:
        parent[node] = find_parent(parent[node])
    return parent[node]
def union(u, v):
    root1 = find_parent(u)
    root2 = find_parent(v)
    parent[root2] = root1

n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(m)]
arr = sorted(arr, key=lambda x:x[2], reverse=True)
start, end = map(int, input().split())
parent = list(range(n+1))

for u, v, weight in arr: # 가중치 큰 것에서부터 내림차순으로 연결(union)하다, start->end가 연결되면, weight 출력 후 정지. 자연스럽게 최대 가능 weight 확인.
    union(u, v)
    print(parent)
    if find_parent(start) == find_parent(end):
        print(weight)
        break