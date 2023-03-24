# 가장 긴 증가하는 부분수열
N = int(input())
arr = list(map(int, input().split()))

DP = [arr[0]]
for num in arr:
    if num > DP[-1]: #
        DP.append(num)
    else:
        for i in range(len(DP)):
            if DP[i] >= num:
                DP[i] = num # 길이만 확인하기 때문에, 자리만 바꿔줘도 무관함. 실제 부분수열과는 다를 수 있음.
                break

print(len(DP))
