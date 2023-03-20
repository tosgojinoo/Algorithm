# 1
def dfs_comb1(now, beginWith): # now: 정해진 지점, beginWith: 이하 분석 지점
    if now == R:
        result.append(picked[:])
        return
    for i in range(beginWith, len(arr)): # now >= beginWith
        # 선정
        picked.append(arr[i])
        dfs_comb1(now+1, i+1)
        # 선정 제외
        picked.pop()

# 2
def dfs_comb2(subset, beginWith, R): # R: 남은 선택지
    if R == 0:
        result.append(subset)
        return

    for ni, nxt in enumerate(arr[beginWith:]):
        dfs_comb2(subset+[nxt], beginWith + ni + 1, R - 1)

R = 3
arr = list(range(4, 10))

picked = []
result = []
dfs_comb1(0, 0)
print(result)

result = []
dfs_comb2([], 0, R)
print(result)


