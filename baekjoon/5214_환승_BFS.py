'''my idea
Dijkstra -> heap 사용하지 않으면, BFS
  - visited = [INF] * N
  - queue = deque([1])
  - cnt = 0
  - while queue:
      - node = queue.popleft()
      - for nnode in arr[node]:
          - if visited[nnode] < cnt:
              - visited[nnode] = cnt

arr[node] = [[nnode]]
for _ in range(M):
  - tmp = input().split()
  - for idx in range(K-1):
      - arr[tmp[idx]].append(tmp[idx+1])
Dijkstra()
print(visited[N] if visited[N] < INF else -1)
'''
from collections import deque
import sys

import sys
from collections import deque

def BFS():
    visited_station = [0 for _ in range(N + 1)]
    visited_htube = [0 for _ in range(M)]  # 시간 초과 방지
    queue = deque()
    queue.append((1, 1))  # station idx, cnt
    visited_station[1] = 1
    while queue:
        s_idx, cnt = queue.popleft()
        next_htube = []
        for h_idx in station[s_idx]:
            if visited_htube[h_idx] == 0:
                next_htube.append(h_idx)
                visited_htube[h_idx] = 1

        for nh_idx in next_htube:
            for h_s_idx in htube[nh_idx]:
                if visited_station[h_s_idx] == 0:
                    if h_s_idx == N:
                        print(cnt + 1)
                        return
                    visited_station[h_s_idx] = 1
                    queue.append((h_s_idx, cnt + 1))

    print(-1)

input = sys.stdin.readline
N, K, M = map(int, input().split()) # 역의 수, 연결하는 역의 개수, 하이퍼튜브의 개수
station = [[] for _ in range(N + 1)]
htube = [[] for _ in range(M)]
for h_idx in range(M):
    temp = list(map(int, input().split()))
    for s_idx in temp:
        station[s_idx].append(h_idx)
        htube[h_idx].append(s_idx)

if N == 1: # ***
    print(1)
else:
    BFS()