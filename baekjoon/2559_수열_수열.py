import sys
input = sys.stdin.readline

def maxsubarraysum():
    result = [sum(arr[:K])]

    for i in range(N - K):
        # sliding window. 맨 앞을 제외, 맨 뒤를 추가
        result.append(result[i] - arr[i] + arr[K + i])

    return result


N, K = map(int, input().split())
arr = list(map(int, input().split()))
# print(arr)
# print(maxsubarraysum())
print(max(maxsubarraysum()))