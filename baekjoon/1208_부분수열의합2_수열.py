def left(start, end):
    sums = [0]
    for index in range(start, end + 1):
        for i in range(len(sums)):
            sums.append(sums[i] + arr[index]) # powerset 패턴
    for current_sum in sums:
        sums_cache[current_sum] = sums_cache.get(current_sum, 0) + 1 # dict에 key가 있으면 가져오고, 아님 0

def right(start, end):
    count = 0
    sums = [0]
    for index in range(start, end + 1):
        for i in range(len(sums)):
            sums.append(sums[i] + arr[index])
    for current_sum in sums:
        count += sums_cache.get(s - current_sum, 0) # 나머지(s-current_sum)가 key로 있으면 가져오기
    return count

n, s = map(int, input().split())
arr = list(map(int, input().split()))
sums_cache = dict()
mid = (0 + n - 1) // 2
left(0, mid) # idx 0 ~ 중간 까지 2개씩 묶어서 더한 값 모임
result = right(mid + 1, n - 1)

if not s:
    print(result - 1)
else:
    print(result)