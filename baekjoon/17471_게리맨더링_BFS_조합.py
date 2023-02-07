# for i in (1~N): # i는 b선거구에 포함시킬 구역의 시작점
#   for step in range(len(N)): # step은 b선거구가 포함하는 구역 개수
#       BFS(step, visited) # 구역 개수 증가시키며, b선거구 구성하는 case 생성 -> 나머지로 r선거구 구성
#       - (sub) BFS(N-step, visited) # b선거구 포함 구역 개수 제외하고, r선거구 구성.
#       - 전부 순회 했는데, 남는 구역이 있을 경우, -1 리턴 & exit()
#       - 아니면, 각 선거구 weight 합의 차이 저장

# => 모든 탐색 필요 없음
# 1~N개 조합으로 구성으로 R그룹 구성 후 각 그룹의 BFS 성공여부 확인 & weight sum 차이 계산

import sys
from collections import deque

input = sys.stdin.readline
def comb(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in comb(arr[i+1:], r-1):
                yield [arr[i]] + nxt

def BFS(group):
    q = deque()
    visited = [False for _ in range(N)]
    q.append(group[0])
    visited[group[0]] = True

    while q:
        node = q.popleft()
        for nnode in range(len(arr[node])):
            if arr[node][nnode] == 0: continue # 이어지지 않음
            if nnode not in group: continue # 그룹에 불포함 구역
            if not visited[nnode]: # 미방문시만 추가 탐색
                visited[nnode] = True
                q.append(nnode)

    return visited.count(True) == len(group) # 방문 총 횟수와 그룹 숫자가 동일해야 성립


def get_total(arr):
    total = 0
    for node in arr:
        total += weights[node]

    return total

N = int(input())
weights = list(map(int, input().split()))
arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    _, *dsts = map(int, input().split())
    for dst in dsts:
        arr[i][dst - 1] = 1 # 2차원 행렬로 구성

cases = []
X = list(range(N))
INF = int(1e9)
ans = INF

for i in range(1, N // 2 + 1): # 절반 만큼만 테스트. 절반 이후 케이스는 R ~ B 그룹 바꾼 것과 동일.
    As = tuple(comb(X, i))
    for A in As:
        B = list(set(X).difference(A)) # X 와 A 간 다른 원소만 표기

        if BFS(A) and BFS(B): # BFS로 둘다 가능하다면
            a_total = get_total(A) # weights sum 계산
            b_total = get_total(B)
            ans = min(ans, abs(a_total - b_total))

print(-1 if ans == INF else ans)