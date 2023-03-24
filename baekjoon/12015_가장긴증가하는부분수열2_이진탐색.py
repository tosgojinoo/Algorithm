import bisect

input()
arr = [int(x) for x in input().split()]
lis = 0
for num in arr:
    i = bisect.bisect_left(arr, num, hi=lis)
    arr[i] = num
    lis += lis <= i

print(lis)