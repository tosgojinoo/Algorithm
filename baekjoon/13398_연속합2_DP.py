# 한개 이상 선택, 가장 큰 합

# Bottom-up, table-filling
# 상태구분: 포함 or 불포함
# DP에는 (이전까지의 연속합 + i번째 원소) or (i번째 원소) 중 큰 값만 저장 => max() 통해 시작점/종료점/연속 구분 가능. 수열에 대한 기억 불필요


import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
DP = [[0] * N for _ in range(2)]
# DP[0][i] : 특정 원소를 제거하지 않은 경우
# DP[1][i] : 특정 원소를 제거한 경우

DP[0][0] = arr[0] # 1개는 반드시 선택해야 한다.

if N > 1:
    ans = -1e9
    for i in range(1, N):
        # 아무런 원소를 제거하지 않았을 때, (이전까지의 연속합 + i번쨰 원소) 와 (i번째 원소)를 비교하여 큰 경우를 대입
        DP[0][i] = max(DP[0][i - 1] + arr[i], arr[i])
        # 특정 원소를 제거하는 경우 => 1. i번째 원소를 제거하는 경우 2. i번째 이전에서 이미 특정 원소를 제거하여 i번째 원소를 선택하는 경우
        # 1의 경우 DP[0][i - 1] 2의 경우 DP[1][i-1] + arr[i]
        DP[1][i] = max(DP[0][i - 1], DP[1][i-1] + arr[i])
        # DP 진행 중 가장 큰 값으로 갱신
        ans = max(ans, DP[0][i], DP[1][i])
    print(ans)
else: # N이 1인 경우는 반드시 선택을 해야하므로 DP[0][0] 출력
    print(DP[0][0])