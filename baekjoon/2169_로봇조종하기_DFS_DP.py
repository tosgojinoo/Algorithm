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