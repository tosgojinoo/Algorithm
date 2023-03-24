N = int(input())
arr = list(map(int, input().split()))

DP = [arr[-1]]

for num in arr[::-1]:
    if num > DP[-1]:
        DP.append(num)
    else:
        for i in range(len(DP)):
            if DP[i] >= num:
                DP[i] = num
                break

print(len(DP))