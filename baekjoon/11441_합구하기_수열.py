import sys
input = sys.stdin.readline

def subarraysum(a, b):
    return prefix_sum[b] - prefix_sum[a-1]

N = int(input())
arr = map(int, input().split())
prefix_sum = [0]
sum = 0
for num in arr:
    sum += num
    prefix_sum.append(sum)

for _ in range(int(input())):
    print(subarraysum(*list(map(int, input().split()))))