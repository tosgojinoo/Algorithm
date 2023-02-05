# 비용행렬
# DP, Top-down

# 모든 경우의 수 확인 => DFS
# DFS(next, visited|(1<<next))
# 해당 노드까지의 가장 최소 금액 저장 => DP
#   - DP[node][visited]: node에서 방문 현황이 visited(비트마스크) 일 때, 방문한 곳을 제외한 나머지 지점들을 들려 시작점까지 되돌아가는 최소 비용 저장
#   - visited => ***** 비트마스킹 (node가 단순증가 index로 구성될 경우 사용. 시간복잡도&메모리 문제로, 적은 제약조건 설정)
#   - visited 의 각 자리수를 통해 방문 node들의 구성으로 된 case 구분
# 점화식
#   - DP[node][visited]
#   = min(DP[node][visited], DP[next][visited | (1 << next)] + arr[node][next])
#   - visited에 next 방문을 추가했을때를 의미함

# 모든 노드 순회 필요 없음. 순환경로(사이클). 출발지점 아무 곳이나 선정.
#   - 1 > 0 > 3 > 2> 1 일 경우, 0 > 3 > 2 > 1 > 0에서도 경로 포함

# def DFS_DP(start):
#   (종료 조건) if visited == (1<<N) - 1:



import sys

input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * (1 << N) for _ in range(N)]

def DFS(node, visited):
    if DP[node][visited] != 0: # 이미 최소비용이 계산되어 있다면, no update
        return DP[node][visited]

    if visited == (1 << N) - 1: # 모든 도시를 방문했다면
        if arr[node][start]: # 출발점으로 가는 경로가 있을 때
            return arr[node][start]
        else: # 출발점으로 가는 경로가 없을 때
            return INF

    min_dist = INF
    for next in range(1, N): # 모든 도시를 탐방
        if not arr[node][next]: # 가는 경로가 없다면 skip
            continue
        if visited & (1 << next): # 이미 방문한 도시라면 skip
            continue
        dist = arr[node][next] + DFS(next, visited | (1 << next)) # DFS를 통해 arr[end][start] 상태로 내려감
        if min_dist > dist: # min() 사용하면 시간초과. if로 계산량 감소.
            min_dist = dist
    DP[node][visited] = min_dist

    return min_dist

start = 0
print(DFS(start, 1))