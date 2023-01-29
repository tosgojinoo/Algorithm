# 계단수: 인접한 모든 자리의 차이는 1
# 0이 아닌 수로 시작

# [순서]
# 점화식
#   - Dn = 'Dn-1' + 'Dn-1[-1] +- 1'
#   - *** 시뮬레이션/그림을 통해 확인
#   - 각 자리수의 경우의 수 == 대각선 위 경우의 수의 합
# dp memory 구현
#   - '0-9 숫자' by 100자리 (2x2 행렬)
# 제한 조건
#   - 1 or 2 포함

n = int(input())
dp = [[0 for i in range(10)] for j in range(101)] # 100 x 10
# init값
for i in range(1, 10):
    dp[1][i] = 1 # 1번째행, 0을 제외한 모든 수에 1 입력
# 점화식 적용
for i in range(2, n + 1): # 자리수
    for j in range(10): # 경우의수
        # 0,9는 가장자리이므로 대각선 위 값이 1개씩
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % 1000000000)
