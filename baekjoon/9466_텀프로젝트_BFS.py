# 끝까지 가봐야 cycle 여부를 확인할 수 있기 때문에, BFS 보다 DFS 로 풀이
'''
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def BFS(x):
    global cycle, result
    q = deque([x])
    visited[x] = 1

    while q:
        x = q.popleft()

        if visited[arr[x]] == 1: # 이전 방문한 곳으로 돌아온 것 확인
            if arr[x] in cycle: # 사이클 가능 여부 확인2
                result += cycle[cycle.index(arr[x]):] # 사이클이 완성되는 되는 구간부터만 저장
        else:
            cycle.append(x)  # 사이클 가능 여부 확인1
            q.append(arr[x])
            visited[arr[x]] = 1


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [False] + list(map(int, input().split()))
    visited = [1] + [0] * N
    result = []
    # 팀 완성되면 출력
    for i in range(1, N+1):
        if visited[i] == 0:
            cycle = []
            BFS(i)

    print(N-len(result)) # cycle 형성한 팀원 제외한 수
'''





