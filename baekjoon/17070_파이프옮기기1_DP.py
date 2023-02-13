''' my idea
DP
'''
'''
DP[state][r][c]
파이프 상태 별로 update 구분
'''

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
DP = [[[0] * N for _ in range(N)] for _ in range(3)] # state: 가로 0, 세로 1, 대각선 2. DP[state][r][c].
DP[0][0][1] = 1  # 첫 시작 위치

# DP를 위해서는 윗 행을 사용해야하므로 첫 행을 먼저 초기화
for i in range(2, N):
    if arr[0][i] == 0: # arr[0][2] != 0 일 경우, DP 초기화 불가
        DP[0][0][i] = DP[0][0][i - 1]

for r in range(1, N):
    for c in range(1, N):
        if arr[r][c] == 0: # 벽이 아닐 때만
            if arr[r][c - 1] == 0 and arr[r - 1][c] == 0: # 대각선만 update
                DP[2][r][c] = DP[0][r - 1][c - 1] + DP[1][r - 1][c - 1] + DP[2][r - 1][c - 1]

            DP[0][r][c] = DP[0][r][c - 1] + DP[2][r][c - 1] # 가로만 update
            DP[1][r][c] = DP[1][r - 1][c] + DP[2][r - 1][c] # 세로만 update

print(sum(DP[i][N - 1][N - 1] for i in range(3)))