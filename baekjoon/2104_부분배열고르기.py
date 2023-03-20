N = int(input())
arr = [*map(int, input().split())] + [0]

presum = [0]
for idx in range(N):
  presum.append(presum[-1] + arr[idx]) # 현재 node 이전까지의 누적합

stack = []
result = 0
for right in range(N+1):
  now = arr[right]
  left = right
  while stack and stack[-1][0] >= now:
    h1, left = stack.pop() # 가장 나중에 추가된 숫자
    result = max(result, (presum[right]-presum[left]) * h1)
  stack.append((now, left))
print(result)