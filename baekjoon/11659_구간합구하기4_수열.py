import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]
sum = 0
for num in arr:
    sum += num
    prefix_sum.append(sum)

for m in range(M):
    i, j = map(int, input().split())
    print(str(prefix_sum[j] - prefix_sum[i-1]))

