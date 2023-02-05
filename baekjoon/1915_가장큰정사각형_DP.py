# arr[n][m] == 1 인 곳에서 DP
# ***** min(arr[n][m-1], arr[n-1][m], arr[n-1][m-1]) 을 DP[n][m]에 저장

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if i>0 and j>0 and arr[i][j] == 1:
            arr[i][j] += min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])
        ans = max(ans, arr[i][j])
print(ans*ans)