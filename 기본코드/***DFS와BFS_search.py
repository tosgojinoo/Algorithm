from collections import deque

def DFS(node):
    for nnode in arr[node]:
        if nnode<=N and not visited[nnode]:
            visited[nnode] = 1
            memory.append(str(nnode))
            DFS(nnode)

def BFS(node):
    queue = deque([node])

    while queue:
        node = queue.popleft()
        for nnode in arr[node]:
            if nnode<=N and not visited[nnode]:
                visited[nnode] = 1
                memory.append(str(nnode))
                queue.append(nnode)

# 정점의 개수 N(1 ≤ N ≤ 1,000)
# 간선의 개수 M(1 ≤ M ≤ 10,000)
# 탐색을 시작할 정점의 번호 V
N, M, V = 5, 5, 3

node_info = [[5, 4],
             [5, 2],
             [1, 2],
             [3, 4],
             [3, 1]]

arr = [[] for _ in range(N+1)]
for i in range(M):
    node, nnode = node_info[i]
    arr[node].append(nnode)
    arr[nnode].append(node)

arr = list(map(sorted, arr))

visited = [0 for _ in range(N+1)]
memory = [str(V)]
visited[V] = 1
DFS(V)
print(' '.join(memory))

visited = [0 for _ in range(N+1)]
memory = [str(V)]
visited[V] = 1
BFS(V)
print(' '.join(memory))