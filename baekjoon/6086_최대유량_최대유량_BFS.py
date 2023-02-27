# 'A'~'Z' => 0~25, 'a'~'z' => 26~51
h = lambda x: ord(x) - ord('A') if x <= 'Z' else ord(x) - ord('a') + 26

def make_flow(S, T, path):
    c = 10**9
    cur = T
    while cur != S:
        c = min(c, capacity[path[cur]][cur] - flow[path[cur]][cur])
        cur = path[cur]
    cur = T
    while cur != S:
        flow[path[cur]][cur] += c
        flow[cur][path[cur]] -= c
        cur = path[cur]
    return c

def BFS(S, T):
    path = [-1] * 52
    queue = [S]
    for u in queue:
        for v in adj[u]:
            if capacity[u][v] - flow[u][v] > 0 and path[v] < 0:
                queue.append(v)
                path[v] = u
                if v == T:
                    return make_flow(S, T, path)
    return 0

def edmonds_karp(S, T):
    max_flow = 0
    while True:
        c = BFS(S, T)
        if c > 0:
            max_flow += c
        else:
            break
    return max_flow


flow = [[0] * 52 for _ in range(52)]
capacity = [[0] * 52 for _ in range(52)]
adj = [[] for _ in range(52)]
N = int(input())
for _ in range(N):
    u, v, c = input().split()
    u, v, c = h(u), h(v), int(c)
    capacity[u][v] += c
    capacity[v][u] += c
    adj[u].append(v)
    adj[v].append(u)
S = h('A')
T = h('Z')
max_flow = edmonds_karp(S, T)
print(max_flow)