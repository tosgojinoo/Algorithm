def maxsubarraysum():
    subarr_sum = arr[0]
    result = arr[0]

    for num in arr[1:]:
        subarr_sum = max(subarr_sum + num, num)
        result = max(result, subarr_sum)

    return result


for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    print(maxsubarraysum())