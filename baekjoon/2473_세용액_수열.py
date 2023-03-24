N = int(input())
arr = sorted(map(int, input().split()))
M = 10**10
for i in range(N-2):
    j, k = i+1, N-1 # 정렬했기 때문에, 항상 arr[i] <= arr[j] <= arr[k]
    while j < k:
        if M > abs(arr[i] + arr[j] + arr[k]):
            M = abs(arr[i] + arr[j] + arr[k])
            i0, j0, k0 = i, j, k
        if arr[i] + arr[j] + arr[k] > 0:
            k -= 1
        else:
            j += 1
print(arr[i0], arr[j0], arr[k0])