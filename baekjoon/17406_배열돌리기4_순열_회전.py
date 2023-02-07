# 회전 연산에 대한 순열 permutation 생성
# 회전 연산 적용
# 행간 합의 최소 계산

def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in permutation(arr[:i]+arr[i+1:], r-1):
                yield [arr[i]] + nxt

def rotate(arr, r, c, s):
    r = r - 1
    c = c - 1

    for radius in range(1, s + 1):
        i = r - radius
        j = c - radius
        tmp = arr[i][j] # 사작점

        # Left side
        while i < r + radius:
            arr[i][j] = arr[i + 1][j]
            i += 1

        # Lower side
        while j < c + radius:
            arr[i][j] = arr[i][j + 1]
            j += 1

        # Right side
        while i > r - radius:
            arr[i][j] = arr[i - 1][j]
            i -= 1

        # Upper side
        while j > c - radius:
            arr[i][j] = arr[i][j - 1]
            j -= 1

        arr[i][j + 1] = tmp

    return arr

def evaluate(arr):
    row_sums = [sum(row) for row in arr]
    return min(row_sums)


N, M, K = map(int, input().split())
arr_init = [list(map(int, input().split())) for _ in range(N)]
rcs = [list(map(int, input().split())) for _ in range(K)]

result = 1e9

# 1. 회전 순서 정하기 (최대 6!=720)
for case in permutation(rcs, K):
    # 2. 회전
    arr = [arr_init[i][:] for i in range(N)] # 복사

    for i in range(K):
        r, c, s = case[i]
        arr = rotate(arr, r, c, s)

    # 3. 각 행의 최소값 찾기
    result = min(result, evaluate(arr))

print(result)