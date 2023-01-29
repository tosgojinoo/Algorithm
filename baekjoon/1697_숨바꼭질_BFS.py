from collections import deque
# DFS는 최소 길이, 최소 거리와 같은 최소 경로를 구하는 데 비효율적
# BFS는 이러한 최소 길이를 구하는 데 있어서 더 효율적

# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)
# 동생은 점 K(0 ≤ K ≤ 100,000)

def BFS(V):
    q = deque([V])
    memory[V] = 1
    while q:
        x = q.popleft()
        if x == K: return print(memory[x]-1)

        for i in [2*x, x+1, x-1]:
            if 0<=i<=100000 and memory[i]==0:
                q.append(i)
                memory[i] = memory[x]+1

N, K = map(int, input().split())
memory = [0]*100001
BFS(N)