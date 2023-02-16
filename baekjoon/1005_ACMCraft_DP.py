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

# input = sys.stdin.readline

def BFS_DP():
    queue = deque()
    for i in range(1, N + 1):
        if inDegree[i] == 0: # 진입차수 0 == 시작 node
            queue.append(i)
            DP[i] = building[i] # 시작 node 부터 DP 시작

    while queue:
        node = queue.popleft()
        for nnode in arr[node]:
            inDegree[nnode] -= 1  # 진입차수 줄이고 갱신
            DP[nnode] = max(DP[node] + building[nnode], DP[nnode]) # 최대 소요시간 저장
            if inDegree[nnode] == 0: # 진입차수 임계 도달
                queue.append(nnode)

    return DP

for _ in range(int(input())):
    N, K = map(int, input().split())
    building = [0] + list(map(int, input().split()))  # 각 건물들의 건설시간. weight.
    inDegree = [0 for _ in range(N + 1)]  # node 실행전 완료되어야 하는 이전 node의 총개수.  # *** DP용 참고 배열
    arr = [[] for _ in range(N + 1)] # node 1부터 시작 위함
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a].append(b)
        inDegree[b] += 1 # 연결 node 증가분 만큼 반영
    DP = [0 for _ in range(N + 1)]  # 해당 건물까지 걸리는 시간

    D = int(input()) # 건설 목표
    DP = BFS_DP()

    print(DP[D])
