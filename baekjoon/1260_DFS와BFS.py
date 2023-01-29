# https://www.acmicpc.net/problem/1260
from collections import deque

def DFS(idx):
    for i in arr[idx]:
        if i<=N and visited[i]==0:
            visited[i]=1
            print(i, end=' ')
            DFS(i)

def BFS(idx):
    q = deque([idx])
    # q.append(idx)

    while q:
        idx = q.popleft()
        for i in arr[idx]:
            if i<=N and visited[i]==0:
                visited[i]=1
                print(i, end=' ')
                q.append(i)

# 정점의 개수 N(1 ≤ N ≤ 1,000)
# 간선의 개수 M(1 ≤ M ≤ 10,000)
# 탐색을 시작할 정점의 번호 V
N,M,V = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    idx, target = map(int, input().split())
    arr[idx].append(target)
    arr[target].append(idx)

arr = list(map(sorted, arr))

visited = [0 for _ in range(N+1)]
print(V, end=' ')
visited[V] = 1
DFS(V)
print()

visited = [0 for _ in range(N+1)]
print(V, end=' ')
visited[V] = 1
BFS(V)