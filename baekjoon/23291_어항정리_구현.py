def roll_fishbowl_array(arr):
    n, t = max(i+1 for i in range(len(arr[0])) if arr[0][i]), []
    if len(arr[0])-n < len(arr):
        return arr
    for i in range(len(arr))[::-1]:
        t += [arr[i][:n]]
        arr[i] = arr[i][n:]
    return roll_fishbowl_array([[*t]+[0]*(len(arr[-1])-len(t)) for t in [*zip(*t)]]+[arr[-1]])

def control_fish_count():
    r, c = len(arr), len(arr[0])
    T = [[0]*c for _ in ' '*r]
    X = [(i, j)for i in range(r)for j in range(c)]
    for i, j in X:
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < r and 0 <= y < c and arr[x][y]:
                t = (arr[i][j]-arr[x][y])//5
                if t > 0:
                    T[i][j] -= t
                    T[x][y] += t
    for i, j in X:
        arr[i][j] += T[i][j]

def serialize_fishbowl_array():
    n, m = len(arr), len(arr[0])
    return [arr[i][j]for j in range(m)for i in range(n)[::-1] if arr[i][j]]

def fold_fishbowl_array(arr, d=0):
    if type(arr[0]) != list:
        arr = [arr]
    n = len(arr[0])//2
    if d == 2:
        return arr
    t = []
    for l in arr[::-1]:
        t += [l[:n][::-1]]
    for l in arr:
        t += [l[n:]]
    return fold_fishbowl_array(t, d+1)



n, k = map(int, input().split()) # 어항 수 N, 가장 많은 <> 적은 어항 물고기 수 차이 K 이하.
arr = [*map(int, input().split())]
A = 1
while A:
    t = min(arr)
    arr = [l + (l == t) for l in arr] # 물고기 수가 최소인 어항 모두에 1개씩 추가
    arr = [[arr[0]]+[0]*(n-2), arr[1:]] # 맨 왼쪽 어항 위로 쌓음 + 0으로 채우기
    arr = roll_fishbowl_array(arr) # 2개 이상 쌓은 어항을 때내어 90도 회전 후 위로 붙임. 이때 밑 바닥에 어항 개수가 충분할 경우 까지만 진행.
    control_fish_count()
    arr = serialize_fishbowl_array()
    arr = fold_fishbowl_array(arr)
    control_fish_count()
    arr = serialize_fishbowl_array()
    if max(arr) - min(arr) <= k:
        break
    A += 1
print(A)