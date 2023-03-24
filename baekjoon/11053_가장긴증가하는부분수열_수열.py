N = int(input())
arr = list(map(int, input().split()))
DP = [arr[0]]

for num in arr:
    if DP[-1] < num:
        DP.append(num)
    else:
        for i in range(len(DP)):
            if DP[i] >= num:
                DP[i] = num
                break

print(len(DP))