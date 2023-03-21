N = int(input())
arr = [*map(int, input().split())] + [0]

presum = [0]
for idx in range(N):
    presum.append(presum[-1] + arr[idx]) # 현재 node 이전까지의 누적합

stack = []
result = 0
for cur in range(N+1):
    now = arr[cur]
    idx = cur
    while stack and stack[-1][0] >= now: # 최대가 되어야하므로, now가 이전 숫자들보다 작아지는 그 이전 지점에서 정산
        height, idx = stack.pop()
        result = max(result, (presum[cur]-presum[idx]) * height)
    stack.append((now, idx)) # (정산 다음 arr값, 정산 기준 idx(arr_idx-1)), 정산하지 않은 값들 쌓임
print(result)