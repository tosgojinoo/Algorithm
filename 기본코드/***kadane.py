def maxSubArraySum(arr):
    subarr_sum = arr[0]
    result = arr[0]

    for num in arr[1:]:
        subarr_sum = max(subarr_sum + num, num)
        result = max(subarr_sum, result)

    return result
arr = [-2, -3, 4, -1, -2, 5, -3]
print("Maximum Sub Array Sum Is", maxSubArraySum(arr))