'''
[설명]
N×M 배열, (1, 1) ~ (N, M)
왼쪽, 오른쪽, 아래쪽 이동, 위쪽 불가
각 지역의 탐사 가치

[문제]
탐사 지역 가치 최대합
'''
'''
[알고리즘]

'''
'''
[구조]

'''




# 3방향 이동(좌, 우, 하). 상 불가.
# 반복 방문 불가.
'''my idea -> x => 매 행마다 각 열에서의 최대값 저장 후 다음으로 전이
DFS_DP(y, x)
  - if y==0 and x==0:
      return arr[y][x]
  visited[y][x] == 1
  - if 0<=ny<N and 0<=nx<M and not visited:
      - memory[y][x] = max(DFS_DP(좌), DFS_DP(위), DFS_DP(우)) -> x
      - ***** 왼쪽 부터 계산해 올 때 or 오른쪽 부터 계산해 올 때. 두가지 경우로 나눠야 함.
  - else:
      return 0

DFS_DP(N-1,M-1) 시작
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rtemp = [0]*M
ltemp = [0]*M


row = list(map(int, input().split()))
ans = [0]*M
ans[0] = row[0]
# 첫 줄은 무조건 오른쪽으로 이동
for i in range(1,M):
    ans[i] = row[i] + ans[i-1]

for _ in range(N-1):
    row = list(map(int, input().split())) # 한줄 입력
    rtemp[0] = ans[0]+row[0] # 오른쪽 이동 init, 위 + 자신(맨 왼쪽)
    ltemp[M-1] = ans[M-1] + row[M-1] # 왼쪽 이동 init, 위 자기자신(맨 오른쪽)
    for i in range(1,M):
        rtemp[i] = max(ans[i],rtemp[i-1]) + row[i] # 위에서 온 것 vs 왼쪽에서 온 것
        ltemp[M-i-1] = max(ans[M-i-1],ltemp[M-i]) + row[M-i-1] # 위에서 온 것 vs 오른쪽에서 온 것
    for i in range(M):
        ans[i] = max(rtemp[i],ltemp[i]) # 왼쪽에서 시작 vs 오른쪽에서 시작. 비교하여 각 지점에서 큰 값 저장.
print(ans[M-1])



'''DFS_DP 방식
import sys

# 재귀깊이 해제
sys.setrecursionlimit(100000)


# DFS_DP : 현재 (x, y)에서 이전 방향이 z였을 때 얻을 수 있는 최대값을 리턴하는 함수
def DFS_DP(x, y, z):
    # Base Case : 오른쪽 아래에 도달한 경우
    if x == n - 1 and y == m - 1:
        return arr[x][y]

    # Memoization
    if DP[x][y][z] != -1:
        return DP[x][y][z]

    # 음의 무한대로 초기화
    DP[x][y][z] = -9876543210

    for i in range(3):
        # nx, ny : 다음 좌표
        nx, ny = x + dx[i], y + dy[i]

        # 오른쪽으로 왔다가 왼쪽으로 가는 경우, 왼쪽으로 왔다가 오른쪽으로 가는 경우는 continue
        if z == 1 and i == 2:
            continue
        if z == 2 and i == 1:
            continue

        # 범위 확인 및 점화식
        if 0 <= nx < n and 0 <= ny < m:
            DP[x][y][z] = max(DP[x][y][z], DFS_DP(nx, ny, i) + arr[x][y])
    return DP[x][y][z]


# 입력부
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# dx, dy : x좌표와 y좌표의 이동배열
dx = [1, 0, 0]
dy = [0, 1, -1]

# DP : 현재 (x, y)에서 이전 방향이 z였을 때 얻을 수 있는 최대값을 저장하는 상태 공간
DP = [[[-1] * 4 for _ in range(m)] for _ in range(n)]

# 정답 출력
print(DFS_DP(0, 0, -1))
print(DP)
'''