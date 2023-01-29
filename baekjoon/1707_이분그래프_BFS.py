import sys
from collections import deque

input = sys.stdin.readline

def BFS(v, group):
    global visited
    q = deque([v])
    visited[v] = group
    while q:
        v = q.popleft()
        for target in arr[v]:
            if visited[target]==0:
                visited[target]=-visited[v]
                q.append(target)
            elif visited[target]==visited[v]:
                return False
    return True

K = int(input()) # test case
for tc in range(K):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        idx, target = map(int, input().split())
        arr[idx].append(target)
        arr[target].append(idx)

    for i in range(1, V+1):
        if visited[i] == 0:
            bipatite = BFS(i, 1) # 처음 시작하는 정점들은 group1
            if not bipatite:
                break

    print("NO" if not bipatite else "YES")
