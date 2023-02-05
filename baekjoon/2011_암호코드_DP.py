# DP, bottom-up, table-filling
# '10 <= arr[N-1] & arr[N] <= 26' 이면 DP[N-2]+ DP[N-1], 아니면 DP[N-1]
# if arr[0] == 0 or arr[N] ==0 and 26 < arr[N-1] & arr[N] -> return -1

import sys
input = sys.stdin.readline
arr = list(input())
N = len(arr)
DP = [0 for _ in range(N + 1)]
DP[0], DP[1] = 1, 1
if arr[0] == "0":
    print(0)
else:
    for i in range(2, N + 1):
        if int(arr[i - 1]) > 0:
            DP[i] += DP[i - 1]
        num = int(arr[i - 1]) + int(arr[i - 2]) * 10
        if num >= 10 and num <= 26:
            DP[i] += DP[i - 2]
    print(DP[N] % 1000000) # N번째만 출력. '30' 같은 경우 걸러짐