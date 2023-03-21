def maxSubArraySum(arr):
    subarr_sum = arr[0]
    result = arr[0]

    for idx in range(1, len(arr)):
        subarr_sum = max(subarr_sum + arr[idx], arr[idx])
        result = max(subarr_sum, result)

    return result
arr = [-2, -3, 4, -1, -2, 5, -3]
print("Maximum Sub Array Sum Is", maxSubArraySum(arr))