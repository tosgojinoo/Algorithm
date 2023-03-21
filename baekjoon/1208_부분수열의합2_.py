def get_sums(start, end):
    sums = [0]
    for index in range(start, end + 1):
        length = len(sums)
        for i in range(length):
            sums.append(sums[i] + sequence[index])

    for current_sum in sums:
        sums_cache[current_sum] = sums_cache.get(current_sum, 0) + 1

def count_sums(start, end):
    count = 0
    sums = [0]
    for index in range(start, end + 1):
        length = len(sums)
        for i in range(length):
            sums.append(sums[i] + sequence[index])
    for current_sum in sums:
        count += sums_cache.get(s - current_sum, 0)
    return count

n, s = map(int, input().split())
sequence = list(map(int, input().split()))
sums_cache = dict()

mid = (0 + n - 1) // 2
get_sums(0, mid)
result = count_sums(mid + 1, n - 1)


if s == 0:
    print(result - 1)
else:
    print(result)