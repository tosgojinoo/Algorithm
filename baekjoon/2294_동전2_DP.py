# N가지 종류, sum = K, 동일 구성에 순서만 다르면 같은 경우로 분류
# 개수 최소

# memory = [[주어진 숫자 개수 만큼] for _ range(3)] => 동일 숫자 재선택 가능하므로, memory x
# DFS&DP 방식, visitied(-1 & sum 저장)
# 주어진 숫자중 3개 선택 & 합은 K
# 1) D1 선택
# 2) K2 = K1 - D1 (K1==K, n==1)
# 3) Kn == 0 = Kn-1 - Dn-1 (X) => dp[i] = min(dp[i - coin]+1

# [순서]
# DFS x
# DP 생성
#   - idx(coin 조합으로 만들 숫자), value(최소 coin 개수)
# 점화식
#   - DPn = min(DP(n-coin)) + 1
#   - ex) DP5 = min(DP4 or DP0) + 1

N, K = map(int, input().split())
coins = []
DP = [0 for idx in range(K + 1)] # *** idx: coin의 조합으로 만들 대상 숫자(0, 1~K), value: K(==idx) 구성하기 위한 coin 개수
for i in range(N):
    coins.append(int(input()))
for idx in range(1, K + 1):
    ans = [] # idx(==K)를 구성하는 coin 조합의 임시 저장소
    for coin in coins:
        if coin <= idx and DP[idx - coin] != -1:
            ans.append(DP[idx - coin])
    if not ans: # coin 조합 미생성, 만들수 없는 경우
        DP[idx] = -1
    else:
        DP[idx] = min(ans) + 1 # coin 조합들 중에 개수가 가장 작은 것 + 1. DP에 coin 개수 저장
print(DP[K])