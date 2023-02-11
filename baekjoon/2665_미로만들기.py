''' my idea
BFS() -> x => 가중치 고려한 간선 우선처리. dijkstra or deque.appendleft() 활용
- visitedied
- memory[bitmask(0~n*n][y][x]

'''
'''
- 벽을 만나는 개수를 가중치가 있는 간선, 없는 간선으로 우선순위 처리
    - 벽 없는 흰방 우선으로 탐색하기 위해, cnt 가중치의 min heap 사용
'''

import sys, heapq

input = sys.stdin.readline
def Dijkstra():
    heap = []
    heapq.heappush(heap, [0, 0, 0])
    visited[0][0] = 1
    while heap: # min heap
        cnt, x, y = heapq.heappop(heap)
        if x == N - 1 and y == N - 1:
            print(cnt) # BFS 방식의 visited 출력과 다름
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if arr[nx][ny] == 0: # 검은 방
                    heapq.heappush(heap, [cnt + 1, nx, ny])
                else:
                    heapq.heappush(heap, [cnt, nx, ny])

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

Dijkstra()