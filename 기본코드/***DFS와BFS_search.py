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

N, M, V = 5, 5, 3 # 정점 N, 간선 M, 탐색 시작 정점 V

node_info = [[5, 4],
             [5, 2],
             [1, 2],
             [3, 4],
             [3, 1]]

arr = [[] for _ in range(N+1)]
for i in range(M): # 양방향
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