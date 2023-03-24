N = int(input())
result = 0
arr = list(map(int, input().split()))
# 누적합
prefix_sum = [arr[0]]
for i in range(1, N):
    prefix_sum.append(prefix_sum[i-1] + arr[i])

# 꿀통과 벌의 거리는 최대한 멀어야 하기 때문에, 벌1은 항상 최대 거리에 위치
# 꿀통이 왼쪽 끝 (+ 벌1 은 오른쪽 끝, 벌2 탐색)
for i in range(1, N-1):
    # 벌1 + 벌2 - 벌2 시작위치(중복제거)
    result = max(result, prefix_sum[N-2] + prefix_sum[i-1] - arr[i])
# 꿀통이 오른쪽 끝 (+ 벌1 은 왼쪽 끝, 벌2 탐색)
for i in range(1, N-1):
    # (벌1: 벌1 - 벌1 시작위치) + (벌2: 전체sum - 벌2 위치) - 벌2 시작위치(중복제거)
    result = max(result, (prefix_sum[N-1] - arr[0]) + (prefix_sum[N-1] - prefix_sum[i]) - arr[i])
# 꿀통 가운데 (+ 벌 양쪽 끝, 꿀통 탐색)
for i in range(1, N-1):
    # 벌1 + 벌2(==0) - 벌2 시작 위치(중복제거) + 꿀통 위치(중복 추가)
    result = max(result, prefix_sum[N-2] - arr[0] + arr[i])
print(result)