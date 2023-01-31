# DP memory 구성
#   - 이전 숫자와 동일하면 제외, 아니면 ans에 추가 x -> DP 방식은 무조건 일단 memory 완성 후 사용


N = int(input())
arr = list(map(int, input().split()))
DP = [1] * N
# DP 구성
for num in range(N):
    for target in range(num):
        if arr[num] > arr[target]:
            DP[num] = max(DP[num], DP[target]+1)

# 최대 수열 길이
order = max(DP)
print(order)

ans = []
# 출력 위한 수열 추출
for i in range(N-1, -1, -1):
    if order == DP[i]:
        ans.append(arr[i])
        order -= 1
ans = reversed(ans)
print(*ans)
