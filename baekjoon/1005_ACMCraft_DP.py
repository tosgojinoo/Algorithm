# 건설 완성까지 Delay
# 동일 step 내 모든 건설이 완료 되어야 다음 step 시작이 가능하므로, Dijksta x DP o
# W 건설 완료시 최소 시간

# T = tc
# N, K = 건물 개수(1~N), 건물간 건설 순서 규칙
# D = 건물단 건설 시간
# X, Y = 건설 순서 X -> Y
# W = 최종 건물 번호

# Dijkstra
#   -w 우선순위, 최대heap 아이디어?
# DP
#   - DP[n] = max(DP[n-1] + W[n], DP[n])

# BFS + DP 
# 이전 node 처리가 완료되어야 진행 가능하므로 BFS 필수
# DP를 이용한 최댓값 저장
# memory 배열 내 이전 입력 값을 활용하면, DP memory
# 동일 step인지 확인 x
#   => *** inDegree 배열로 진입차수(이전 node 개수 총합) 저장 및 참고
#   => step 별로 정렬해서 볼 필요 없음

import sys
from collections import deque

input = sys.stdin.readline

def BFS_DP():
    DP = [0 for _ in range(N + 1)]  # 해당 건물까지 걸리는 시간
    q = deque()
    for i in range(1, N + 1):
        if inDegree[i] == 0: # 진입차수 0 == 시작node
            q.append(i)
            DP[i] = building[i]

    while q:
        a = q.popleft()
        for i in arr[a]:
            inDegree[i] -= 1  # 진입차수 줄이고 갱신
            # DP
            DP[i] = max(DP[a] + building[i], DP[i])
            if inDegree[i] == 0:
                q.append(i)

    return DP

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    building = [0] + list(map(int, input().split()))  # 각 건물들의 건설시간
    inDegree = [0 for _ in range(N + 1)]  # 진입차수 == 이전 노드의 총개수, # *** DP용 참고 배열

    arr = [[] for _ in range(N + 1)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a].append(b)
        inDegree[b] += 1

    D = int(input())
    DP = BFS_DP()

    print(DP[D])
