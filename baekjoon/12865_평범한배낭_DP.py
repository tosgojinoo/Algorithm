N, K = map(int, input().split())
DP = [0]*(K+1)
for _ in range(N):
    weight, value = map(int, input().split())
    for tot_weight in range(K, weight - 1, -1): # idx: weight, DP[idx] = value
        DP[tot_weight] = max(DP[tot_weight-weight] + value, DP[tot_weight]) # 이전무게 + 추가가치 or 현재총가치
print(DP[K])