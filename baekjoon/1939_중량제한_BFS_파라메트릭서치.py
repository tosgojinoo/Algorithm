'''
파라메트릭 서치. 매개 변수 탐색.
'''
from collections import deque
import sys

input = sys.stdin.readline


def BFS(weight):  # weight == now
    queue = deque([one])
    visited = [False] * (n + 1)
    visited[one] = True

    while queue:
        node = queue.popleft()  # w == limit

        for nnode, w in arr[node]:
            if not visited[nnode] and w >= weight:
                visited[nnode] = True
                queue.append(nnode)

    if visited[two]: # 탐색 종료했는데, 다음 공장에 도달 했다면 True.
        return True
    else:
        return False


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]

for i in range(m):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
    arr[v].append([u, w])

one, two = map(int, input().split())

start = 1
end = 1000000000

result = 0
while start <= end: # 탐색 범위가 교차되는 순간, 중지(파라메트릭 서치)
    mid = (start + end) // 2

    if BFS(mid): # 지나갈 수 있을 때, 범위를 위로 조정
        result = mid
        start = mid + 1
    else: # 지나갈 수 없을 때, 범위를 아래로 조정
        end = mid - 1

print(result)